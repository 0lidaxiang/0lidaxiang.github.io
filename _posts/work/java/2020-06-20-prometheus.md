---
layout: post
title:  "漫谈 prometheus"
rootCate: "work"
categories:
- architecture
tags:
- work
- user_permisstion
- architecture
---

以下应用是基于 Springboot 项目的监控，如果是 Springboot 2 版本，可以安装 mircrometer 组件来提供对 prometheus 的支持。
<!---more--->

## Can use 4 kinds of metrics
Prometheus 中提供了四种指标类型（参考：Prometheus 的指标类型），Counter、Timer、 以及直方图（Histogram）和摘要（Summary），后两者是最复杂和难以理解的.

例如Histogram 会在一段时间范围内对数据进行采样（通常是请求持续时间或响应大小等），并将其计入可配置的存储桶（bucket）。


## Prometheus Commands Exampls
以下命令更适合与 Grafana 搭配使用。

Sub-Interface QPS (rate 10s, status=200)
```
rate(http_server_requests_seconds_count{application="PROJECT", uri!="/actuator/prometheus" ,status="200"}[1m]) 
```

Sub-Interface Latency P90 (rate 1min , seconds)
'''
 histogram_quantile(0.9, sum(rate(http_server_requests_seconds_bucket{application="PROJECT_NAME", uri!="/actuator/prometheus"}[1m])) by (uri, le)) 
'''


Sub-Interface Latency P50 (rate 1min , seconds)
```
 histogram_quantile(0.5, sum(rate(http_server_requests_seconds_bucket{application="PROJECT_NAME", uri!="/actuator/prometheus"}[1m])) by ( uri, le)) 
```

TOP URL Visits
```
 topk(10, sum( http_server_requests_seconds_count{application="PROJECT_NAME",uri!="/actuator/prometheus"}) by (uri))
```

HTTP methods Count
```
  sum(http_server_requests_seconds_count {application="PROJECT_NAME", uri!="/actuator/prometheus"}) by (status)
```

Log Count By Level
```
topk(5,  sum(logback_events_total{application="PROJECT_NAME"}) by (level))
```