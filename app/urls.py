from django.urls import path
from .views import home, project_list, project_detail, blog_list, blog_detail, skill_list, skill_detail, experience_list, experience_detail, faq_list, faq_detail

urlpatterns = [
    path('', home, name='home'),

    # Projects URLs
    path('projects/', project_list, name='project_list'),
    path('projects/<slug:slug>/', project_detail, name='project_detail'),

    # Blogs URLs
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),

    # Skills URLs
    path('skills/', skill_list, name='skill_list'),
    path('skills/<slug:slug>/', skill_detail, name='skill_detail'),

    # Experience URLs
    path('experience/', experience_list, name='experience_list'),
    path('experience/<slug:slug>/', experience_detail, name='experience_detail'),

    # FAQs
    path('faqs/', faq_list, name='faq_list'),
    path('faqs/<slug:slug>/', faq_list, name='faq_detail'),
]
