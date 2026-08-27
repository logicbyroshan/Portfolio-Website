from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse, JsonResponse
from django.views.generic import RedirectView
from app.sitemaps import StaticViewSitemap, ProjectSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
    'blogs': BlogSitemap,
}

def health_check(request):
    return JsonResponse({"status": "ok", "service": "DevMeet Portfolio"})

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
    path('api/health/', health_check, name='health_check'),
    path('api/v1/health/', health_check, name='health_check_v1'),
    path('login/', RedirectView.as_view(url=f'/{admin_path}', permanent=False), name='legacy_login'),
    path('admin/', RedirectView.as_view(url=f'/{admin_path}', permanent=False), name='legacy_admin'),
    path(admin_path, admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom HTTP Error Handlers
handler404 = 'app.views.custom_404_view'
handler500 = 'app.views.custom_500_view'
handler403 = 'app.views.custom_403_view'
handler400 = 'app.views.custom_400_view'
