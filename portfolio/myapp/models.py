from django.db import models

from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_image = models.ImageField(upload_to='projects/')  # Main project image
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    link3 = models.URLField(max_length=200, blank=True)
    problem = models.TextField(null=True, blank=True)  # Problem description
    solution = models.TextField(null=True, blank=True)  # Solution description
    skills_used = models.CharField(max_length=500, null=True, blank=True)  # Comma-separated skills
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ImageField(upload_to='projects/slider/')

    def __str__(self):
        return f"Slider Image for {self.project.title}"

class ProjectFeature(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='features')
    feature = models.CharField(max_length=255)

    def __str__(self):
        return f"Feature of {self.project.title}: {self.feature}"



class Skills(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    image = models.ImageField(upload_to='skills/')
    description = models.TextField()
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    link = models.URLField(max_length=200, blank=True)
    date = models.DateField()
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='expericence/')
    link = models.URLField(max_length=200, blank=True)
    date1 = models.DateField()
    date2 = models.DateField()
    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    def __str__(self):
        return self.question

class Meinfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='meinfo/')
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Hobby(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='hobby/')
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='education/')
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.name

