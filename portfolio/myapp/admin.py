from django.contrib import admin
from .models import Projects, Skills, Blogs, Experience, Contact, FAQ, ProjectImage, ProjectFeature

# Register your models here.
admin.site.register(Projects)
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 5  # Number of extra image fields

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 6  # Number of extra feature fields

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ProjectFeatureInline]
    list_display = ('title', 'start_date', 'end_date')


admin.site.register(Skills)
admin.site.register(Blogs)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(FAQ)
