---
layout: default
title: "目录　Outline"
permalink: /workOutline/
---


{% assign groups = site.posts | group_by: "categories" | sort: "name" %}

<div id='cat_cloud'>
{% for group in groups %}
{% assign group_name = group.name | remove: '["' | remove: '"]'  %}

{% if group_name == 'work' %}
<a href="#{{ group_name }}" title="{{ group_name }}" rel="{{  group.items.size }}">{{ group_name }}  ({{ group.items.size }})</a>

{% endif %}
{% endfor %}
</div>

{% for group in groups %}
{% assign group_name = group.name | remove: '["' | remove: '"]'  %}

{% if group_name == 'work' %}
<h2>{{ group_name }}</h2>
  <ol>
		{% for post in group.items %}
			<li><a href="{{ post.url }}">{{ post.title  }}</a> - {{ post.date | date: "%b %-d, %Y" }}</li>
		{% endfor %}
	</ol>
  {% endif %}
{% endfor %}

<a href="#" class="top">Top</a>
