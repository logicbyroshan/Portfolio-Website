from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link1 = models.URLField(max_length=200, blank=True)
    link2 = models.URLField(max_length=200, blank=True)
    link3 = models.URLField(max_length=200, blank=True)
    def __str__(self):
        return self.title


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