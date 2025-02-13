from django.shortcuts import render, get_object_or_404
from .models import Project, Blog, Skill, Experience, FAQ, Resume
from django.http import FileResponse
import os
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    email,  # Sender's email
                    ['contact@roshandamor.site'],  # Receiver (your email)
                    fail_silently=False,
                )
                return JsonResponse({"status": "success", "message": "Your message has been sent!"})
            except:
                return JsonResponse({"status": "error", "message": "Failed to send message. Try again later."})
        else:
            return JsonResponse({"status": "error", "message": "Invalid form data. Please check your inputs."})

    return JsonResponse({"status": "error", "message": "Invalid request method."})

# Download Resume
def download_resume(request):
    resume_path = os.path.join(settings.MEDIA_ROOT, 'resume.pdf')  # Ensure this path is correct
    if os.path.exists(resume_path):
        return FileResponse(open(resume_path, 'rb'), as_attachment=True)
    else:
        raise Http404("Resume not found")

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

    projects = Project.objects.prefetch_related("images").all()[:6]
    blogs = Blog.objects.all()[:6]
    skills = Skill.objects.all()[:6]
    experiences = Experience.objects.all()[:3]

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
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

# Blog Views
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})

# Skill Views
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

# Experience Views
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'experiences.html', {'experiences': experiences})

# FAQs View
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs.html', {'faqs': faqs})

