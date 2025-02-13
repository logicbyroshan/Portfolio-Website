from django.shortcuts import render, get_object_or_404
from .models import Project, Blog, Skill, Experience, FAQ

# Home View - Shows limited content (6 items per section)
def home(request):
    section = request.GET.get("section", "faq")  # Default to FAQs
    category = request.GET.get("category", "All")  # Default category filter
    sort_order = request.GET.get("sort", "latest")  # Default sorting (latest)

    faqs = FAQ.objects.all()
    
    if section == "faq":
        # Filter by category
        if category != "All":
            faqs = faqs.filter(category=category)

        # Apply sorting
        if sort_order == "oldest":
            faqs = faqs.order_by("created_at")  # Oldest first
        else:
            faqs = faqs.order_by("-created_at")  # Newest first

    else:
        faqs = FAQ.objects.all()[:6]  # Default case (show 6 FAQs)

    projects = Project.objects.all()[:6]
    blogs = Blog.objects.all()[:6]
    skills = Skill.objects.all()[:6]
    experiences = Experience.objects.all()[:6]

    categories = FAQ.objects.values_list('category', flat=True).distinct()  # Get unique categories

    return render(request, 'portfolio-landing-page.html', {
        'projects': projects,
        'blogs': blogs,
        'skills': skills,
        'experiences': experiences,
        'faqs': faqs,
        'faq_categories': categories,  # Pass categories for filtering
        'selected_category': category,  # Pass selected category for UI
        'sort_order': sort_order,  # Pass selected sorting for UI
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
