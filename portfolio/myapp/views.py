from django.shortcuts import render
from urllib import request
from django.views import View
from django.http import HttpResponse
from .models import Skills  # Ensure this matches your model name
from .models import Projects  # Ensure this matches your model name
from .models import Blogs  # Ensure this matches your model name
from .models import Expericence  # Ensure this matches your model name



def home(request):
    return render(request, 'home.html')

class SkillsView(View):
    def get(self, request):
        # Fetch all skills from the database
        skills = Skills.objects.all()  # Using the correct model name
        # Render the template with the skills data
        return render(request, 'skills.html', {'skills': skills})

    
class ProjectsView(View):
    def get(self, request):
        # Fetch all projects from the database
        projects = Projects.objects.all()  # Using the correct model name
        # Render the template with the projects data
        return render(request, 'project.html', {'projects': projects})

class BlogsView(View):
    def get(self, request):
        # Fetch all blogs from the database
        blogs = Blogs.objects.all()  # Using the correct model name
        # Render the template with the blogs data
        return render(request, 'blogs.html', {'blogs': blogs})

class ExpericenceView(View):
    def get(self, request):
        # Fetch all expericence from the database
        expericence = Expericence.objects.all()  # Using the correct model name
        # Render the template with the expericence data
        return render(request, 'experience.html', {'expericence': expericence})