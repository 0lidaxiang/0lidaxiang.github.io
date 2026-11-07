require "jekyll"
require_relative "../_plugins/optimized_images"

photos = {
  "/assets/images/test.jpg" => {
    "variants" => [
      { "path" => "/assets/img/optimized/test-640.webp", "width" => 640, "height" => 480 },
      { "path" => "/assets/img/optimized/test-1280.webp", "width" => 1280, "height" => 960 },
    ],
  },
}
render = ->(html, baseurl = "") { Lidaxiang::OptimizedImages.render(html, photos, baseurl) }

# Keep both the original destination and the image's accessible text.
original = %(<p><img src="/assets/images/test.jpg" alt="山 &amp; 海"></p>)
html = render.call(original)
raise "Original link lost" unless html.include?('href="/assets/images/test.jpg"')
raise "Alt changed" unless html.include?('alt="山 &amp; 海"')
raise "Width candidates missing" unless html.include?("640w,") && html.include?("1280w")
raise "Intrinsic ratio missing" unless html.include?('width="1280" height="960"')
raise "First photo delayed" unless html.include?('loading="eager"')
raise "Not idempotent" unless render.call(html) == html

# Existing links and authored responsive images must not acquire nested anchors.
linked = %(<a href="/gallery/"><img src='/assets/images/test.jpg' alt='相片'></a>)
html = render.call(linked)
raise "Nested original link" unless html.scan(/<a\b/).size == 1 && html.include?('href="/gallery/"')
responsive = %(<img src="/assets/images/test.jpg" srcset="/custom.webp 640w">)
raise "Explicit responsive image changed" unless render.call(responsive) == responsive
data_source = %(<img data-src="/assets/images/test.jpg" src="/placeholder.png">)
raise "Placeholder data attribute rewritten" unless render.call(data_source) == data_source

# Native lazy loading reserves geometry and works without JavaScript.
html = render.call(original + original)
raise "Below-fold image not lazy" unless html.scan('loading="lazy"').size == 1
raise "Async decoding missing" unless html.scan('decoding="async"').size == 2

# Deploying to a subdirectory must prefix both previews and full-size links.
html = render.call(original.gsub("/assets/", "/blog/assets/"), "/blog")
raise "Subpath original lost" unless html.include?('href="/blog/assets/images/test.jpg"')
raise "Subpath candidate missing" unless html.include?("/blog/assets/img/optimized/test-640.webp 640w")
raise "External image changed" unless render.call('<img src="https://example.com/a.jpg">') == '<img src="https://example.com/a.jpg">'
puts "PASS: original links, alt text, srcset, geometry, lazy loading, existing links, idempotence and baseurl"
