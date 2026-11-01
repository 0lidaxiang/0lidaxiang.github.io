---
layout: outline_tag
title: "生活目录　Outline"
permalink: /lifeOutline/
---

{% assign groups = site.posts | group_by: "categories" | sort: "name" %}
<nav class="archive-filters" aria-label="文章分类">
{% for group in groups %}
  {% assign group_name = group.name | remove: '["' | remove: '"]' %}
  {% assign count = 0 %}
  {% for post in group.items %}{% if post.rootCate != 'work' %}{% assign count = count | plus: 1 %}{% endif %}{% endfor %}
  {% if count > 0 %}<a href="#category-{{ group_name | slugify }}-{{ forloop.index }}">{{ group_name }} <span>({{ count }})</span></a>{% endif %}
{% endfor %}
</nav>
{% for group in groups %}
  {% assign group_name = group.name | remove: '["' | remove: '"]' %}
  {% assign count = 0 %}
  {% for post in group.items %}{% if post.rootCate != 'work' %}{% assign count = count | plus: 1 %}{% endif %}{% endfor %}
  {% if count > 0 %}
<section aria-labelledby="category-{{ group_name | slugify }}-{{ forloop.index }}">
  <h2 id="category-{{ group_name | slugify }}-{{ forloop.index }}" class="hr-bottom">{{ group_name }}</h2>
  <ul class="related-posts">
  {% for post in group.items %}
    {% if post.rootCate != 'work' %}{% include_cached components/post-list-item.html post=post format="%Y-%m-%d" %}{% endif %}
  {% endfor %}
  </ul>
</section>
  {% endif %}
{% endfor %}
