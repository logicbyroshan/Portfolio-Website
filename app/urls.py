from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, project_list, project_detail, blog_list, blog_detail, 
    skill_list, experience_list, get_resume, download_resume, user_terms_view,
    skill_icon_lookup
)

urlpatterns = [
    path('', home, name='home'),

    # Projects URLs (with slug for detail view)
    path('projects/', project_list, name='project_list'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),

    # Blogs URLs (with slug for detail view)
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),

    # Skills (No detail page)
    path('skills/', skill_list, name='skill_list'),

    # Experience (No detail page)
    path('experience/', experience_list, name='experience_list'),



    path("resume/", get_resume, name="resume"),
    path("resume/download/", download_resume, name="download_resume"),
    path("user-terms/", user_terms_view, name="user_terms"),
    path("api/skill-icon-lookup/", skill_icon_lookup, name="skill_icon_lookup"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)