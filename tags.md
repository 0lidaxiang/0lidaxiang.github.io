---
layout: outline_tag
title: "标签　Tags"
permalink: /tags/
---

<nav class="archive-filters" aria-label="文章标签">
{% assign sorted_tags = site.tags | sort %}
{% for tag in sorted_tags %}
  <a href="#tag-{{ tag[0] | slugify }}-{{ forloop.index }}">{{ tag[0] }} <span>({{ tag[1].size }})</span></a>
{% endfor %}
</nav>
{% for tag in sorted_tags %}
<section aria-labelledby="tag-{{ tag[0] | slugify }}-{{ forloop.index }}">
  <h2 id="tag-{{ tag[0] | slugify }}-{{ forloop.index }}" class="hr-bottom">{{ tag[0] }}</h2>
  <ul class="related-posts">
  {% for post in tag[1] %}
    {% include_cached components/post-list-item.html post=post format="%Y-%m-%d" %}
  {% endfor %}
  </ul>
</section>
{% endfor %}
