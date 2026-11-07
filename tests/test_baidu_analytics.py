"""Check API contracts and statistics semantics without credentials or network."""
from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "stats", Path(__file__).resolve().parents[1] / "scripts/sync_baidu_analytics.py")
stats = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stats)

SITE = "https://www.lidaxiang.cn"
TRACKER = "a" * 32
SITE_LIST = {"list": [{"site_id": 123, "domain": "www.lidaxiang.cn", "status": 0,
                        "create_time": "2026-11-01 12:00:00"}]}


def summary(fields, values):
    return {"result": {"fields": ["simple_date_title", *fields],
                       "sum": [values, []], "total": 1}}


def page_report(urls, counts, total=None):
    return {"result": {"fields": ["visit_page_title", "pv_count"],
                       "total": len(urls) if total is None else total,
                       "items": [[[({"name": url})] for url in urls],
                                 [[count] for count in counts], [], []]}}


class AnalyticsTest(unittest.TestCase):
    def test_shanghai_today_pagination_and_url_aggregation(self):
        replies = [SITE_LIST, summary(["pv_count"], [1000]),
                   summary(["pv_count", "visitor_count"], [30, 7]),
                   page_report([SITE + "/ai/中文/?utm_source=test", SITE + "/ai/%E4%B8%AD%E6%96%87"], [5, 8], 3),
                   page_report([SITE + "/other"], [2], 3)]
        with patch.object(stats, "request_json", side_effect=replies) as request:
            data = stats.export_counts("private-token", TRACKER, SITE, now=datetime(
                2026, 11, 6, 16, 30, tzinfo=timezone.utc))
        self.assertEqual((data["date"], data["total_pv"], data["today_pv"], data["today_uv"]),
                         ("2026-11-07", 1000, 30, 7))
        self.assertEqual(data["pages"]["/ai/中文"], 13)
        calls = request.call_args_list
        self.assertEqual(calls[2].args[1]["start_date"], "20261107")
        self.assertEqual(calls[4].args[1]["start_index"], 2)
        self.assertNotIn("private-token", str(data))

    def test_accepts_reordered_metrics(self):
        self.assertEqual(stats.report_summary(summary(
            ["visitor_count", "pv_count"], [7, "1,234"])["result"]),
            {"visitor_count": 7, "pv_count": 1234})

    def test_empty_report_is_zero_but_missing_data_is_not(self):
        self.assertEqual(stats.report_summary({"fields": ["date", "pv_count"], "total": 0}), {"pv_count": 0})
        with self.assertRaises(stats.AnalyticsError):
            stats.report_summary(summary(["pv_count"], ["--"])["result"])
        for value in [None, -1, 1.5, True]:
            with self.assertRaises(stats.AnalyticsError):
                stats.count(value)

    def test_normalizes_same_site_only(self):
        self.assertEqual(stats.normalize_page("http://lidaxiang.cn/ai/post/?x=1#heading", SITE), "/ai/post")
        self.assertEqual(stats.normalize_page(SITE + "/index.html", SITE), "/")
        self.assertIsNone(stats.normalize_page("https://elsewhere.example/ai/post", SITE))
        with self.assertRaises(stats.AnalyticsError):
            stats.normalize_page("A page title", SITE)

    def test_does_not_publish_another_site_or_subdirectory(self):
        sites = {"list": [dict(SITE_LIST["list"][0], domain="other.example"),
                          dict(SITE_LIST["list"][0], domain="www.lidaxiang.cn/ai")]}
        with patch.object(stats, "request_json", return_value=sites):
            with self.assertRaises(stats.AnalyticsError):
                stats.export_counts("token", TRACKER, SITE)
        with patch.object(stats, "request_json", return_value=SITE_LIST):
            with self.assertRaises(stats.AnalyticsError):
                stats.export_counts("token", TRACKER, SITE, site_id="999")

    def test_incomplete_page_report_fails_instead_of_zeroing_articles(self):
        replies = [SITE_LIST, summary(["pv_count"], [100]),
                   summary(["pv_count", "visitor_count"], [10, 5]),
                   page_report([], [], 3)]
        with patch.object(stats, "request_json", side_effect=replies):
            with self.assertRaises(stats.AnalyticsError):
                stats.export_counts("token", TRACKER, SITE)

    def test_authentication_never_uses_client_credentials_grant(self):
        with patch.object(stats, "request_json", return_value={"access_token": "new-token"}) as request:
            token = stats.access_token({"BAIDU_API_KEY": "key", "BAIDU_SECRET_KEY": "secret",
                                        "BAIDU_REFRESH_TOKEN": "refresh"})
        self.assertEqual(token, "new-token")
        self.assertEqual(request.call_args.args[1]["grant_type"], "refresh_token")
        self.assertTrue(request.call_args.kwargs["post"])
        self.assertIsNone(stats.access_token({}))
        with self.assertRaises(stats.AnalyticsError):
            stats.access_token({"BAIDU_API_KEY": "key"})

    def test_fallback_accepts_same_tracker_and_only_public_fields(self):
        snapshot = dict(tracking_id=TRACKER, available=True, site_id="123", start_date="20261101",
                        date="2026-11-07", updated_at="2026-11-07 10:00", total_pv=100,
                        today_pv=10, today_uv=5, pages={}, access_token="must-not-publish")
        with patch.object(stats, "request_json", return_value=snapshot):
            self.assertNotIn("access_token", stats.previous_snapshot(SITE, TRACKER))
            self.assertIsNone(stats.previous_snapshot(SITE, "b" * 32))


if __name__ == "__main__":
    unittest.main()
