#!/usr/bin/env python3
"""Export aggregate Baidu Tongji counts at build time; never publish credentials."""
import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode, urlsplit
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
API = "https://openapi.baidu.com/rest/2.0/tongji/"
SHANGHAI = ZoneInfo("Asia/Shanghai")
COUNT_KEYS = ("total_pv", "today_pv", "today_uv")


class AnalyticsError(Exception):
    pass


def request_json(url, params=None, *, post=False):
    encoded = urlencode(params or {}).encode()
    request = Request(
        url if post or not params else url + "?" + encoded.decode(),
        data=encoded if post else None,
        headers={"User-Agent": "lidaxiang-blog-stats/1.0"},
    )
    try:
        with urlopen(request, timeout=30) as response:
            data = json.load(response)
    except (HTTPError, URLError, TimeoutError, ValueError) as error:
        # Exception URLs and API payloads may contain credentials: never log them.
        raise AnalyticsError("百度统计请求失败，请检查授权或网络") from error
    if not isinstance(data, dict) or data.get("error_code") or data.get("error"):
        raise AnalyticsError("百度统计返回错误，请检查 API 权限及授权有效期")
    return data


def access_token(environ):
    credentials = [environ.get(name, "") for name in (
        "BAIDU_API_KEY", "BAIDU_SECRET_KEY", "BAIDU_REFRESH_TOKEN")]
    if all(credentials):
        api_key, secret_key, refresh_token = credentials
        response = request_json("https://openapi.baidu.com/oauth/2.0/token", {
            "grant_type": "refresh_token", "client_id": api_key,
            "client_secret": secret_key, "refresh_token": refresh_token,
        }, post=True)
        token = response.get("access_token")
        if not isinstance(token, str) or not token:
            raise AnalyticsError("百度统计未返回有效的访问令牌")
        return token
    if environ.get("BAIDU_ACCESS_TOKEN"):
        return environ["BAIDU_ACCESS_TOKEN"]
    if any(credentials):
        raise AnalyticsError("百度统计授权配置不完整，需要 API Key、Secret Key 和 Refresh Token")
    return None


def host_name(url):
    parsed = urlsplit(url if "://" in url else "https://" + url)
    return (parsed.hostname or "").lower().removeprefix("www.")


def domain_path(url):
    return urlsplit(url if "://" in url else "https://" + url).path


def normalize_page(url, site_url):
    parsed = urlsplit(url)
    if parsed.hostname and host_name(url) != host_name(site_url):
        return None
    if not parsed.hostname and not url.startswith("/"):
        raise AnalyticsError("受访页面报告没有返回可识别的页面地址")
    path = unquote(parsed.path) or "/"
    if path.endswith("/index.html"):
        path = path[:-10]
    return path.rstrip("/") or "/"


def count(value):
    # Zero is a valid count; missing or invalid data must not silently become zero.
    if isinstance(value, bool):
        raise AnalyticsError("统计指标格式无效")
    raw = str(value).replace(",", "")
    if not re.fullmatch(r"\d+", raw):
        raise AnalyticsError("统计指标缺失或格式无效")
    return int(raw)


def metric_values(result, values):
    fields = [field for field in result.get("fields", [])
              if field in ("pv_count", "visitor_count")]
    if not fields or len(fields) != len(values):
        raise AnalyticsError("统计指标与报告字段不匹配")
    return dict(zip(fields, map(count, values)))


def report_summary(result):
    try:
        if result.get("total") == 0:
            return {field: 0 for field in result["fields"]
                    if field in ("pv_count", "visitor_count")}
        return metric_values(result, result["sum"][0])
    except (KeyError, IndexError, TypeError) as error:
        raise AnalyticsError("统计报告缺少汇总数据") from error


def export_counts(token, tracking_id, site_url, site_id="", now=None):
    now = now or datetime.now(SHANGHAI)
    now = now.astimezone(SHANGHAI)
    today = now.strftime("%Y%m%d")
    sites = request_json(API + "config/getSiteList", {"access_token": token}).get("list", [])
    matches = [site for site in sites
               if host_name(str(site.get("domain", ""))) == host_name(site_url)
               and domain_path(site["domain"]) in ("", "/")
               and (not site_id or str(site.get("site_id")) == site_id)]
    if len(matches) != 1:
        raise AnalyticsError("无法唯一匹配本站，请检查 BAIDU_SITE_ID 及站点域名")
    site = matches[0]
    if site.get("status") != 0:
        raise AnalyticsError("百度统计站点已暂停")
    try:
        start_date = datetime.strptime(site["create_time"][:10], "%Y-%m-%d").strftime("%Y%m%d")
    except (KeyError, ValueError, TypeError) as error:
        raise AnalyticsError("无法确定百度统计站点的创建日期") from error
    if start_date > today:
        raise AnalyticsError("百度统计站点创建日期晚于当前日期")

    def report(method, metrics, start, **extra):
        response = request_json(API + "report/getData", {
            "access_token": token, "site_id": site["site_id"],
            "method": method, "metrics": metrics,
            "start_date": start, "end_date": today, **extra,
        })
        result = response.get("result")
        if not isinstance(result, dict):
            raise AnalyticsError("百度统计未返回报告数据")
        return result

    total = report_summary(report("trend/time/a", "pv_count", start_date,
                                  gran="day", max_results=1))
    daily = report_summary(report("trend/time/a", "pv_count,visitor_count", today,
                                  gran="day", max_results=1))
    pages = {}
    offset = 0
    while True:
        result = report("visit/toppage/a", "pv_count", start_date,
                        start_index=offset, max_results=200, order="pv_count,desc")
        try:
            dimensions, rows = result["items"][:2]
            total_rows = count(result["total"])
            if len(dimensions) != len(rows) or (not rows and offset < total_rows):
                raise AnalyticsError("受访页面报告不完整")
            for dimension, values in zip(dimensions, rows):
                item = dimension[0]
                url = (item.get("url") or item.get("name")) if isinstance(item, dict) else item
                path = normalize_page(url, site_url)
                if path is not None:
                    pages[path] = pages.get(path, 0) + metric_values(result, values)["pv_count"]
            offset += len(rows)
        except (KeyError, IndexError, TypeError, ValueError) as error:
            raise AnalyticsError("受访页面报告结构无效") from error
        if offset >= total_rows:
            break

    return {
        "tracking_id": tracking_id, "available": True,
        "site_id": str(site["site_id"]), "start_date": start_date,
        "date": now.strftime("%Y-%m-%d"),
        "updated_at": now.strftime("%Y-%m-%d %H:%M"),
        "total_pv": total["pv_count"], "today_pv": daily["pv_count"],
        "today_uv": daily["visitor_count"], "pages": pages,
    }


def previous_snapshot(site_url, tracking_id):
    """Keep the last deployed counts if a temporary API problem occurs."""
    try:
        data = request_json(site_url.rstrip("/") + "/assets/data/baidu-analytics.json")
        if data.get("available") and data.get("tracking_id") == tracking_id:
            for key in COUNT_KEYS:
                count(data[key])
            # Explicit allow-list: publish only aggregate counts, never raw API payloads.
            return {key: data[key] for key in (
                "tracking_id", "available", "site_id", "start_date", "date",
                "updated_at", *COUNT_KEYS, "pages")}
    except (AnalyticsError, KeyError, TypeError):
        pass
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", default="https://www.lidaxiang.cn")
    args = parser.parse_args()
    source = ROOT / "_data/baidu_analytics.json"
    data = json.loads(source.read_text())
    tracking_id = os.environ.get("BAIDU_TRACKING_ID") or data["tracking_id"]
    if not re.fullmatch(r"[a-fA-F0-9]{32}", tracking_id):
        raise SystemExit("百度统计站点标识无效")
    data["tracking_id"] = tracking_id
    try:
        token = access_token(os.environ)
        if token:
            data = export_counts(token, tracking_id, args.site_url,
                                 os.environ.get("BAIDU_SITE_ID", ""))
            print("百度统计汇总与文章浏览量同步完成。")
        else:
            print("尚未配置百度统计 API 授权；先启用访问采集，保留原访问量展示。")
            data = previous_snapshot(args.site_url, tracking_id) or data
    except AnalyticsError as error:
        print(f"::warning::{error}；保留上次统计快照。", file=sys.stderr)
        data = previous_snapshot(args.site_url, tracking_id) or data
    # Write both copies only after all reports have succeeded or fallback was selected.
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    source.write_text(payload)
    public = ROOT / "assets/data/baidu-analytics.json"
    public.parent.mkdir(parents=True, exist_ok=True)
    public.write_text(payload)


if __name__ == "__main__":
    main()
