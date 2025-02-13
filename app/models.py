from django.db import models
from django.utils.text import slugify
import math
import datetime

# Model for Skill
class Skill(models.Model):
    STATUS_CHOICES = [
        ("Expert", "Expert"),
        ("Learning", "Learning"),
        ("Average", "Average"),
    ]

    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to="skills/icons/", blank=True, null=True)  # Allow skills without icons
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Learning")
    level = models.PositiveIntegerField(default=50)  # Skill level out of 100
    description = models.TextField(max_length=500, blank=True)  # Make description optional
    created_at = models.DateTimeField(auto_now_add=True)  # Track when a skill is added
    updated_at = models.DateTimeField(auto_now=True)  # Track modifications

    class Meta:
        ordering = ["-level", "name"]  # Show highest-level skills first

    def __str__(self):
        return f"{self.name} ({self.level}%)"



class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    skills = models.ManyToManyField("Skill", related_name="project_skills")
    slug = models.SlugField(unique=True, blank=True)

    # ✅ Allow blank values to avoid IntegrityError
    problem_statement = models.TextField(max_length=500, null=True, blank=True)
    solution = models.TextField(max_length=500, null=True, blank=True)
    impact = models.TextField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/images/")

    def __str__(self):
        return f"Image for {self.project.title}"

class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="features")
    image = models.ImageField(upload_to="projects/features/")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.project.title}"

class Learning(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="learnings")
    paragraph = models.TextField(max_length=255)

    def __str__(self):
        return f"Learning for {self.project.title}"


# Model for Experience
class Experience(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="experience/")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Allow null for ongoing experiences
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update on modification

    class Meta:
        ordering = ["-start_date"]  # Most recent experiences first

    def __str__(self):
        return self.title


# Blog Model (Kept as it is)
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/")
    publication_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    
    categories = models.CharField(max_length=255, help_text="Separate categories with commas", default="Uncategorized")  # ✅ Multiple categories
    time_to_read = models.PositiveIntegerField(default=1, editable=False)  # ✅ Auto-calculated time

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Generate slug automatically
        
        self.time_to_read = self.calculate_reading_time()  # Auto-calculate reading time
        super().save(*args, **kwargs)

    def calculate_reading_time(self):
        words_per_minute = 200  # Average reading speed
        word_count = len(self.content.split())  # Count words in content
        return max(1, math.ceil(word_count / words_per_minute))  # At least 1 min

    def get_category_list(self):
        return [cat.strip() for cat in self.categories.split(',')]  # ✅ Convert to list

    def __str__(self):
        return self.title

# FAQ Model
class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('Job', 'Job'),
        ('Tech', 'Tech'),
        ('Freelance', 'Freelance'),
        ('General', 'General'),
    ]

    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General')
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for sorting

    class Meta:
        ordering = ['-created_at']  # Default sorting (newest first)

    def __str__(self):
        return self.question
