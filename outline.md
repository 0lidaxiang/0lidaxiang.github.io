---
layout: default
permalink: /outline/
---

<div id='cat_cloud'>
{% for cat in site.categories %}
<a href="#{{ cat[0] }}" title="{{ cat[0] }}" rel="{{ cat[1].size }}">{{ cat[0] }}  ({{ cat[1].size }})</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
{% endfor %}
</div>


{% for cat in site.categories %}
<ul class="listing">
  <h2  id="{{ cat[0] }}">{{ cat[0] }} </h2>
{% for post in cat[1] %}
  <li class="listing-item">
  <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
  <a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>
{% endfor %}
