from django.shortcuts import render
from urllib import request
from django.views import View
from django.http import HttpResponse
from .models import Skills
from .models import Projects
from .models import Blogs
from .models import Experience
from .models import FAQ
from .models import Hobby
from .models import Contact
from .models import Meinfo
from .models import Education





def home(request):
    blogs = Blogs.objects.all()[:3]  # Get the first 3 blogs
    projects = Projects.objects.all()[:3]  # Get the first 3 projects
    skills = Skills.objects.all()[:12]  # Get the first 3 skills
    expericence = Experience.objects.all()[:3]  # Get the first 3 experiences
    faqs = FAQ.objects.all()  # Fetch all FAQs (since you want all of them)

    context = {
        'blogs': blogs,
        'projects': projects,
        'skills': skills,
        'expericence': expericence,
        'faqs': faqs,
    }
    return render(request, 'home.html', context)


class SkillsView(View):
    def get(self, request):
        skills = Skills.objects.all()  # Using the correct model name
        return render(request, 'skills.html', {'skills': skills})

    
class ProjectsView(View):
    def get(self, request):
        projects = Projects.objects.all()  # Using the correct model name
        return render(request, 'project.html', {'projects': projects})

class BlogsView(View):
    def get(self, request):
        blogs = Blogs.objects.all()  # Using the correct model name
        return render(request, 'blogs.html', {'blogs': blogs})

class ExperienceView(View):
    def get(self, request):
        expericence = Experience.objects.all()
        return render(request, 'experience.html', {'expericence': expericence})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'proeject-page.html', {'project': project})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog-page.html', {'blog': blog})

def experience_detail(request, id):
    experience = get_object_or_404(Experience, id=id)
    return render(request, 'experience-page.html', {'experience': experience})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project-page.html', {'project': project})

class MeinfoView(View):
    def get(self, request):
        meinfo = Meinfo.objects.all()
        return render(request, 'personal.html', {'meinfo': meinfo})

class EducationView(View):
    def get(self, request):
        education = Education.objects.all()
        return render(request, 'education.html', {'education': education})

class HobbyView(View):
    def get(self, request):
        hobbies = Hobby.objects.all()
        return render(request, 'hobbies.html', {'hobbies': hobbies})

