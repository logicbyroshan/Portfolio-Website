from django.shortcuts import render, get_object_or_404
from .models import Project, Blog, Skill, Experience, FAQ

# Home View - Shows limited content (6 items per section)
def home(request):
    projects = Project.objects.all()[:6]
    blogs = Blog.objects.all()[:6]
    skills = Skill.objects.all()[:6]
    experiences = Experience.objects.all()[:6]
    faqs = FAQ.objects.all()[:6]
    
    return render(request, 'portfolio-landing-page.html', {
        'projects': projects,
        'blogs': blogs,
        'skills': skills,
        'experiences': experiences,
        'faqs': faqs
    })

# Project Views
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})

# Blog Views
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'portfolio/blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'portfolio/blog_detail.html', {'blog': blog})

# Skill Views
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skill.html', {'skills': skills})

def skill_detail(request, slug):
    skill = get_object_or_404(Skill, slug=slug)
    return render(request, 'portfolio/skill_detail.html', {'skill': skill})

# Experience Views
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience_list.html', {'experiences': experiences})

def experience_detail(request, slug):
    experience = get_object_or_404(Experience, slug=slug)
    return render(request, 'portfolio/experience_detail.html', {'experience': experience})

# FAQs View
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'portfolio/faq_list.html', {'faqs': faqs})

def faq_detail(request, slug):
    faq = get_object_or_404(FAQ, slug=slug)
    return render(request, 'portfolio/faq_detail.html', {'faq': faq})
