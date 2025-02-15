from django.shortcuts import render
from .models import Project, Blog, Skill, Experience, FAQ
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # ✅ Fix: Use your authorized email as sender
            send_mail(
                subject=contact_message.subject,
                message=f"Message from {contact_message.name} ({contact_message.email}):\n\n{contact_message.message}",
                from_email="contact@roshandamor.site",  # ✅ Use your actual email
                recipient_list=["contact@roshandamor.site"],  # ✅ Ensure recipient is correct
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "portfolio-landing-page.html", {"form": form})




def get_unique_categories(queryset, field_name):
    """Extract unique categories from a given model field."""
    categories = set()
    for obj in queryset.values_list(field_name, flat=True):
        if obj:  # Ensure the category field is not empty or None
            for cat in obj.split(","):  # Split comma-separated categories
                clean_cat = cat.strip()
                if clean_cat and clean_cat.lower() != "uncategorized":  # Exclude "Uncategorized"
                    categories.add(clean_cat)
    return sorted(categories)  # Return sorted distinct categories

def home(request):
    sort_by = request.GET.get("sort", "-publication_date")  
    category = request.GET.get("category", "")

    # Fetch all data
    projects = Project.objects.prefetch_related("images").all()
    blogs = Blog.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    faqs = FAQ.objects.all()

    # Apply filtering based on category
    if category:
        projects = projects.filter(Q(categories__icontains=category))
        blogs = blogs.filter(Q(categories__icontains=category))
        skills = skills.filter(Q(categories__icontains=category))
        experiences = experiences.filter(Q(categories__icontains=category))
        faqs = faqs.filter(Q(categories__icontains=category))

    # Apply sorting dynamically
    projects = projects.order_by(sort_by)[:6]
    blogs = blogs.order_by(sort_by)[:6]
    skills = skills.order_by("-level")[:6]
    experiences = experiences.order_by("-start_date")[:3]
    faqs = faqs.order_by("-created_at")[:6]

    # Get distinct categories for all sections
    blog_categories = get_unique_categories(Blog.objects, "categories")
    project_categories = get_unique_categories(Project.objects, "categories")
    faq_categories = get_unique_categories(FAQ.objects, "categories")
    skill_categories = get_unique_categories(Skill.objects, "categories")
    experience_categories = get_unique_categories(Experience.objects, "categories")

    return render(request, "portfolio-landing-page.html", {
        "projects": projects,
        "blogs": blogs,
        "skills": skills,
        "experiences": experiences,
        "faqs": faqs,
        "selected_category": category,
        "selected_sort": sort_by,
        "blog_categories": blog_categories,
        "project_categories": project_categories,
        "faq_categories": faq_categories,
        "skill_categories": skill_categories,
        "experience_categories": experience_categories,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project-detail.html', {'project': project})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog-detail.html', {'blog': blog})


# Project Views
def project_list(request):
    query = request.GET.get('search', '')  # Fix for URL issue
    category = request.GET.get('category', '')  # Category filter
    sort_by = request.GET.get('sort', '-created_at')  # Default sorting by newest first

    projects = Project.objects.all()
    categories = Project.objects.values_list('categories', flat=True).distinct()  # ✅ Get all categories

    if query:
        projects = projects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if category and category != "all":  # ✅ Ensure "all" option works
        projects = projects.filter(categories__icontains=category)

    if sort_by == 'oldest':
        projects = projects.order_by('created_at')
    else:
        projects = projects.order_by('-created_at')

    return render(request, 'projects.html', {
        'projects': projects, 'query': query, 'category': category, 'sort_by': sort_by, 'categories': categories
    })


# Blog Views
def blog_list(request):
    query = request.GET.get('search', '')  # Fix for URL issue
    category = request.GET.get('category', '')  # Category filter
    sort_by = request.GET.get('sort', '-publication_date')  

    blogs = Blog.objects.all()
    categories = Blog.objects.values_list('categories', flat=True).distinct()  # ✅ Get all categories

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    if category and category != "all":  
        blogs = blogs.filter(categories__icontains=category)

    if sort_by == 'oldest':
        blogs = blogs.order_by('publication_date')
    else:
        blogs = blogs.order_by('-publication_date')

    return render(request, 'blogs.html', {
        'blogs': blogs, 'query': query, 'category': category, 'sort_by': sort_by, 'categories': categories
    })


# Skill Views
def skill_list(request):
    query = request.GET.get('search', '')  # Fix for URL issue
    category = request.GET.get('category', '')  
    sort_by = request.GET.get('sort', 'name')  

    skills = Skill.objects.all()
    categories = Skill.objects.values_list('categories', flat=True).distinct()  # ✅ Get all categories

    if query:
        skills = skills.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if category and category != "all":  
        skills = skills.filter(categories__icontains=category)

    if sort_by == 'level':
        skills = skills.order_by('-level')  
    elif sort_by == 'name':
        skills = skills.order_by('name')

    return render(request, 'skills.html', {
        'skills': skills, 'query': query, 'category': category, 'sort_by': sort_by, 'categories': categories
    })


# Experience Views
def experience_list(request):
    query = request.GET.get('search', '')  # Fix for URL issue
    category = request.GET.get('category', '')
    sort_by = request.GET.get('sort', '-start_date')  

    experiences = Experience.objects.all()
    categories = Experience.objects.values_list('categories', flat=True).distinct()  # ✅ Get all categories

    if query:
        experiences = experiences.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if category and category != "all":  
        experiences = experiences.filter(categories__icontains=category)

    if sort_by == 'oldest':
        experiences = experiences.order_by('start_date')
    else:
        experiences = experiences.order_by('-start_date')

    return render(request, 'experiences.html', {
        'experiences': experiences, 'query': query, 'category': category, 'sort_by': sort_by, 'categories': categories
    })


# FAQs View
def faq_list(request):
    query = request.GET.get('search', '')
    category = request.GET.get('category', '')
    sort_by = request.GET.get('sort', '-created_at')  

    faqs = FAQ.objects.all()
    categories = FAQ.objects.values_list('categories', flat=True).distinct()

    if query:
        faqs = faqs.filter(
            Q(question__icontains=query) | Q(answer__icontains=query)
        )

    if category and category != "all":  
        faqs = faqs.filter(categories__icontains=category)

    if sort_by == 'oldest':
        faqs = faqs.order_by('created_at')
    else:
        faqs = faqs.order_by('-created_at')

    return render(request, 'faqs.html', {
        'faqs': faqs, 'query': query, 'category': category, 'sort_by': sort_by, 'categories': categories
    })
