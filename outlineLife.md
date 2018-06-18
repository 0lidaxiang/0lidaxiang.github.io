---
layout: outline_tag
title: "生活目录　Outline"
permalink: /lifeOutline/
---

{% assign groups = site.posts | group_by: "categories" | sort: "name" %}

<div id='cat_cloud'>
{% for group in groups %}
{% assign group_name = group.name | remove: '["' | remove: '"]'  %}

{% for post in group.items %}
{% if post.rootCate != 'work' %}
  <a href="#{{ group_name }}" title="{{ group_name }}" rel="{{  group.items.size }}">{{ group_name }} ({{ group.items.size }}) — </a>
  {% break %}
  {% endif %}
{% endfor %}
{% endfor %}
</div>

<!-- <div style="width:100%;height: auto;margin-top:20px;"> -->
{% for group in groups %}
{% assign group_name = group.name | remove: '["' | remove: '"]'  %}

  <div style="width:100%;height: auto;margin-top:20px;">
  <ul class="listing">
  {% for post in group.items %}


  {% if post.rootCate != 'work' %}
    <h2>{{ group_name }}</h2>
    {% break %}
    {% endif %}
  {% endfor %}

  {% for post in group.items %}
      {% if post.rootCate != 'work' %}
  			<li  class="listing-item"><a href="{{ post.url }}">{{ post.title  }}</a> - {{ post.date | date: "%b %-d, %Y" }}</li>
        {% endif %}
  {% endfor %}
  </ul>
{% endfor %}

</div>
