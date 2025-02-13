from django.contrib import admin
from .models import Project, Skill, Experience, Blog, ProjectImage, Feature, Learning, FAQ, Resume

admin.site.register(Resume)

class ProjectImageInline(admin.TabularInline):  # or admin.StackedInline
    model = ProjectImage
    extra = 1  # Number of empty fields shown

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

class LearningInline(admin.TabularInline):
    model = Learning
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "publication_date", "slug")
    inlines = [ProjectImageInline, FeatureInline, LearningInline]  # Embed related models

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image")

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "project")

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ("paragraph", "project")
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Blog)
admin.site.register(FAQ) 