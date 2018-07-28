"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap

sitemaps = {
	'posts':PostSitemap
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='sitemap'),
    url(r'^post/(?P<post_id>[0-9]+)/{0,1}$', views.blog_detail, name='blog_detail'),
    url(r'^search/tag/(?P<tag_str>[A-Za-z0-9 ]+)/(?P<page_num>[0-9]+)/{0,1}$', views.blog_tag_search,
        name='blog_tag_search'),
    url(r'^search/(?P<search_str>[A-Za-z0-9 ]*)/(?P<page_num>[0-9]+)/{0,1}$', views.blog_search,
        name='blog_search'),
    url(r'^no_results/{0,1}$', views.no_results, name='no_results'),
    url(r'^category/(?P<cat_id>[1-9]+)/(?P<page_num>[1-9]+)$',
        views.blog_category, name='blog_cat'),
]
