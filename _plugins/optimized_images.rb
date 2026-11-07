# Use checked-in previews at render time; preserve historical Markdown and image URLs.
require "cgi"

module Lidaxiang
  module OptimizedImages
    SIZES = "(max-width: 42em) calc(100vw - 3rem), (max-width: 64em) calc(100vw - 6rem), 54rem".freeze

    def self.render(html, photos, baseurl = "")
      inside_link = false
      photo_count = 0
      html.gsub(%r{</?a\b[^>]*>|<img\b[^>]*>}i) do |tag|
        if tag.match?(%r{\A</a\b}i)
          inside_link = false
          next tag
        elsif tag.match?(/\A<a\b/i)
          inside_link = true
          next tag
        end
        source = tag.match(/(?<=\s)src\s*=\s*(["'])(.*?)\1/i)
        next tag unless source
        url = CGI.unescapeHTML(source[2])
        next tag unless baseurl.empty? || url.start_with?(baseurl + "/")
        path = baseurl.empty? ? url : url.delete_prefix(baseurl)
        # Explicit responsive images remain under the author's control.
        entry = photos[path]
        next tag unless entry && !tag.match?(/(?<=\s)srcset\s*=/i)
        variants = entry.fetch("variants")
        largest = variants.max_by { |image| image.fetch("width") }
        photo_count += 1
        srcset = variants.map { |image| "#{baseurl}#{image.fetch('path')} #{image.fetch('width')}w" }.join(", ")
        image = tag.sub(source[0], %(src="#{CGI.escapeHTML(baseurl + largest.fetch('path'))}"))
        attributes = {
          "srcset" => srcset, "sizes" => SIZES,
          "width" => largest.fetch("width"), "height" => largest.fetch("height"),
          "loading" => photo_count == 1 ? "eager" : "lazy", "decoding" => "async",
        }
        attributes.each do |name, value|
          next if image.match?(/(?<=\s)#{name}\s*=/i)
          image = image.sub(%r{\s*/?>\z}, %( #{name}="#{CGI.escapeHTML(value.to_s)}">))
        end
        next image if inside_link
        %(<a href="#{CGI.escapeHTML(url)}" target="_blank" rel="noopener" aria-label="查看照片原图（新窗口）">#{image}</a>)
      end
    end
  end
end

Jekyll::Hooks.register [:documents, :pages], :post_convert do |item|
  photos = item.site.data.dig("optimized_images", "photos")
  next unless photos && item.content.include?("<img")
  item.content = Lidaxiang::OptimizedImages.render(item.content, photos, item.site.baseurl.to_s)
end
