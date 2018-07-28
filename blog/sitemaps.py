from django.contrib.sitemaps import Sitemap
from .models import Post, Tag, Category

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    def items(self):
        return Post.objects.all()

    def lastmod(self,obj):
        return obj.pub_date

    def location(self, obj):
        return '/blog/'+str(obj.pk)

