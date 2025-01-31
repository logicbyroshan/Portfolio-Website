from django.db import models
from django.utils.text import slugify

# Model for Skill
class Skill(models.Model):
    STATUS_CHOICES = [
        ('Expert', 'Expert'),
        ('Learning', 'Learning'),
        ('Average', 'Average'),
    ]

    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to="skills/icons/")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Learning')
    level = models.PositiveIntegerField(default=50)  # Skill level out of 100
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

# Model for Project
class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255)  # Store as comma-separated tags
    images = models.ManyToManyField("ProjectImage", related_name="project_images")  # Multiple images
    description = models.TextField(max_length=500)
    skills = models.ManyToManyField(Skill, related_name="project_skills")  # Multiple skills
    slug = models.SlugField(unique=True, blank=True)  # For clean URLs

    # Features with images, title, and description
    features = models.ManyToManyField("Feature", related_name="project_features")
    
    # Learnings as list of paragraphs
    learnings = models.ManyToManyField("Learning", related_name="project_learnings")
    
    # Problem, solution, and impact sections
    problem_statement = models.TextField(max_length=500)
    solution = models.TextField(max_length=500)
    impact = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)  # Generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model for Project Images
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/images/")

    def __str__(self):
        return f"Image for {self.project.title}"

# Model for Features of a Project
class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/features/")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.project.title}"

# Model for Learnings in a Project
class Learning(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    paragraph = models.TextField(max_length=30)  # Max 30 words per paragraph

    def __str__(self):
        return f"Learning for {self.project.title}"

# Model for Experience
class Experience(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="experience/")
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

# Blog Model (Kept as it is)
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs/")
    publication_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question