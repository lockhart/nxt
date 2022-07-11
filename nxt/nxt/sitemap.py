# -*- coding: utf-8 -*-
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from membership.models import Profile


class PagesSitemap(Sitemap):
    """
    Declare all static pages which should appear in the site map.
    """
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['nxt:home', 'nxt:about', 'membership:profile']

    def location(self, page):
        return reverse(page)
    pass


class ProfileSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Profile.objects.all()

    def lastmod(self, obj):
        return obj.updated
    pass
