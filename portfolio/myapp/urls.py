from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path("my-skills/", views.SkillsView.as_view(), name="skills"),
    path("my-projects/", views.ProjectsView.as_view(), name="projects"),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path("my-blogs/", views.BlogsView.as_view(), name="blogs"),
    path("my-experience/", views.ExperienceView.as_view(), name="experience"),
    path("my-personal/", views.MeinfoView.as_view(), name="meinfo"),
    path("education/", views.EducationView.as_view(), name="education"),
    path("hobbies/", views.HobbyView.as_view(), name="hobbies"),
    
]
