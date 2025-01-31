from django.contrib import admin
from .models import Project, Skill, Experience, Blog, ProjectImage, Feature, Learning, FAQ

admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Feature)
admin.site.register(Learning)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Blog)
admin.site.register(FAQ) 