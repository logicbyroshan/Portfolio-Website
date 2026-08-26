from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project, Blog

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'project_list', 'blog_list', 'skill_list', 'experience_list', 'faq_list', 'user_terms']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Project.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('project_detail', kwargs={'slug': obj.slug})

class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Blog.objects.all().order_by('-publication_date')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('blog_detail', kwargs={'slug': obj.slug})
