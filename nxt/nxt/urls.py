from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from .views import HomeView, AboutView
from .sitemap import PagesSitemap, ProfileSitemap

admin.site.site_header = "NXT administration"

sitemaps = {"profiles": ProfileSitemap,
            "static": PagesSitemap}

# put the top-level URLs into a separate list to allow namespacing as "nxt:"
nxtpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("about/", AboutView.as_view(), name="about"),
    path("", HomeView.as_view(), name="home"),
]

urlpatterns = [
    path("membership/", include(("membership.urls", "membership"), namespace="membership")),
    path('admin/', admin.site.urls),
    path('social/', include('social_django.urls', namespace='social')),
    path('', include((nxtpatterns, 'nxt'), namespace='nxt')),
]
