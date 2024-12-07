from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path("my-skills/", views.SkillsView.as_view(), name="skills"),
    path("my-projects/", views.ProjectsView.as_view(), name="projects"),
    path("my-blogs/", views.BlogsView.as_view(), name="blogs"),
    path("my-experience/", views.ExperienceView.as_view(), name="experience"),
]
