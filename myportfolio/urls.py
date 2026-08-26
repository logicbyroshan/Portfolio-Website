from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from app.sitemaps import StaticViewSitemap, ProjectSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
    'blogs': BlogSitemap,
}

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /dash-admin/",
        "Disallow: /tinymce/",
        "",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

admin_path = getattr(settings, 'ADMIN_URL', 'dash-admin/').strip('/') + '/'

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path(admin_path, admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
