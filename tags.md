---
layout: outline_tag
title: "标签　Tags"
permalink: /tags/
---

<div id='tag_cloud' style="height: auto;">
{% assign first = site.tags.first %}
{% assign max = first[1].size %}
{% assign min = max %}
{% for tag in site.tags offset:1 %}
  {% if tag[1].size > max %}
    {% assign max = tag[1].size %}
  {% elsif tag[1].size < min %}
    {% assign min = tag[1].size %}
  {% endif %}
{% endfor %}
{% assign diff = max | minus: min %}


<style>

.cpanel div.icon div{-moz-transition-duration: 0.8s;background-color: #FFFFFF;background-position: -30px 50%;border: 1px solid #CCCCCC;color: #565656;display: block;float: left;text-align:center;text-indent:0;}
.cpanel div.icon span:hover{border:1px solid blue;}
</style>


<div class="cpanel" style="width: 100%;height: 400px;">
<!-- {{ max  | times: site.tags.size }}px -->
    <div class="icon">
    {% for tag in site.tags %}
      {% assign temp = tag[1].size | minus: min | times: 36 | divided_by: diff %}
      {% assign base = temp | divided_by: 4 %}
      {% assign remain = temp | modulo: 4 %}
      {% if remain == 0 %}
        {% assign size = base | plus: 9 %}
      {% elsif remain == 1 or remain == 2 %}
        {% assign size = base | plus: 9 | append: '.5' %}
      {% else %}
        {% assign size = base | plus: 10 %}
      {% endif %}
      {% if remain == 0 or remain == 1 %}
        {% assign color = 9 | minus: base %}
      {% else %}
        {% assign color = 8 | minus: base %}
      {% endif %}

      <div style="border-radius: {{ size | times: 3}}px;height: {{ size | times: 5}}px;width: {{ size | times: 5}}px;margin-left: 20pt;">
      <a href="#{{ tag[0] }}" style="font-size: {{ size }}pt; color: #{{ color }}{{ color }}{{ color }};" title="{{ tag[0] }}" rel="{{ tag[1].size }}">{{ tag[0] }}
      </a>
      <!-- <a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}">{{ tag[0] }} ({{ tag[1].size }})</a> -->
      </div>
    {% endfor %}

    </div>
    </div>
</div>

<div style="width:100%;height: auto;margin-top:20px;">
{% for tag in site.tags %}
<ul class="listing">
  <h2  id="{{ tag[0] }}">{{ tag[0] }} </h2>
{% for post in tag[1] %}
  <li class="listing-item">
  <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
  <a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
{% endfor %}
</div>
