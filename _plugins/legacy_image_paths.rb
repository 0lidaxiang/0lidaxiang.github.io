# Preserve historical /images URLs without changing the Markdown or duplicating source images.
module Lidaxiang
  class LegacyLightworksImage < Jekyll::StaticFile
    def destination(dest)
      File.join(dest, "images", "work", "lightworks", name)
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  dir = "assets/images/work/lightworks"
  %w[add-transition.png modify-video-saturation.png].each do |name|
    site.static_files << Lidaxiang::LegacyLightworksImage.new(site, site.source, dir, name)
  end
end
