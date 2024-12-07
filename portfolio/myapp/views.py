from django.shortcuts import render
from urllib import request
from django.views import View
from django.http import HttpResponse
from .models import Skills  # Ensure this matches your model name
from .models import Projects  # Ensure this matches your model name
from .models import Blogs  # Ensure this matches your model name
from .models import Experience  # Ensure this matches your model name
from .models import FAQ  # Ensure this matches your model name



def home(request):
    blogs = Blogs.objects.all()[:3]  # Get the first 3 blogs
    projects = Projects.objects.all()[:3]  # Get the first 3 projects
    skills = Skills.objects.all()[:8]  # Get the first 3 skills
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
