from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.utils import timezone
import tempfile
import shutil
from app.models import Project, Blog, Skill, Experience, FAQ, Resume, ContactMessage
from app.views import get_unique_categories

MEDIA_TEMP_DIR = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_TEMP_DIR)
class ComprehensivePortfolioTests(TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA_TEMP_DIR, ignore_errors=True)

    def setUp(self):
        self.client = Client()
        self.skill1 = Skill.objects.create(name="Python", level=90, status="Expert", categories="Backend, Core")
        self.skill2 = Skill.objects.create(name="C++", level=85, status="Expert", categories="Systems, Performance")
        self.skill3 = Skill.objects.create(name="Django", level=95, status="Expert", categories="Backend, Web")

        self.project1 = Project.objects.create(
            title="DevMeet Platform",
            categories="Web, Full-Stack, C++",
            tags="Python, Django, WebSockets",
            description="A real-time developer platform"
        )
        self.project1.skills.add(self.skill1, self.skill3)

        self.project2 = Project.objects.create(
            title="DevMeet Platform", # Test slug collision handling
            categories="AI/ML, Web",
            tags="Python, PyTorch",
            description="Duplicate title to verify slug suffix generation"
        )

        self.blog1 = Blog.objects.create(
            title="Clean Architecture Principles in Python",
            categories="Architecture, C++, Backend",
            content="<p>Detailed architecture breakdown with more than twenty words to test reading time calculation properly.</p>",
            image="blogs/dell-8pb7Hq539Zw-unsplash.webp"
        )

        self.blog2 = Blog.objects.create(
            title="Clean Architecture Principles in Python", # Test slug collision
            categories="Best Practices, Architecture",
            content="<p>Another article with duplicate title.</p>",
            image="blogs/dell-8pb7Hq539Zw-unsplash.webp"
        )

        self.exp = Experience.objects.create(
            title="Senior Software Engineer",
            image="experience/Google.webp",
            start_date="2024-01-01",
            categories="Engineering, Cloud",
            description="Architecting microservices and distributed backend systems."
        )

        self.faq = FAQ.objects.create(
            question="Are you available for freelance projects?",
            answer="Yes, I am actively available for select projects and technical consulting.",
            categories="General, Freelance"
        )

    def test_home_page_renders_successfully(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Roshan Damor")
        self.assertContains(response, "DevMeet Platform")
        self.assertContains(response, "Clean Architecture Principles")

    def test_project_slug_collision_resolution(self):
        self.assertEqual(self.project1.slug, "devmeet-platform")
        self.assertEqual(self.project2.slug, "devmeet-platform-1")

    def test_blog_slug_collision_and_reading_time(self):
        self.assertEqual(self.blog1.slug, "clean-architecture-principles-in-python")
        self.assertEqual(self.blog2.slug, "clean-architecture-principles-in-python-1")
        self.assertGreaterEqual(self.blog1.time_to_read, 1)

    def test_project_list_and_detail_with_special_characters(self):
        # Test listing
        res_list = self.client.get(reverse('project_list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, "DevMeet Platform")

        # Test search query
        res_search = self.client.get(reverse('project_list') + '?search=real-time')
        self.assertEqual(res_search.status_code, 200)
        self.assertContains(res_search, "DevMeet Platform")

        # Test category filter
        res_cat = self.client.get(reverse('project_list') + '?category=Full-Stack')
        self.assertEqual(res_cat.status_code, 200)
        self.assertContains(res_cat, "DevMeet Platform")

        # Test detail view with special char category (C++)
        res_detail = self.client.get(reverse('project_detail', kwargs={'slug': self.project1.slug}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, "DevMeet Platform")

    def test_blog_list_and_detail_with_special_characters(self):
        res_list = self.client.get(reverse('blog_list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, "Clean Architecture Principles")

        # Test detail view
        res_detail = self.client.get(reverse('blog_detail', kwargs={'slug': self.blog1.slug}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, "Clean Architecture Principles")

    def test_skills_list_and_sorting(self):
        res_level = self.client.get(reverse('skill_list') + '?sort=level')
        self.assertEqual(res_level.status_code, 200)
        self.assertContains(res_level, "Django")

        res_name = self.client.get(reverse('skill_list') + '?sort=name')
        self.assertEqual(res_name.status_code, 200)
        self.assertContains(res_name, "C++")

    def test_experience_list(self):
        response = self.client.get(reverse('experience_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Senior Software Engineer")

    def test_faq_home_rendering_and_max_6_limit(self):
        from django.core.exceptions import ValidationError
        from app.admin import FAQAdmin
        from django.contrib.admin.sites import AdminSite

        # Check FAQ on home page
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you available for freelance projects?")

        # Create up to 6 FAQs
        current_count = FAQ.objects.count()
        for i in range(current_count, 6):
            FAQ.objects.create(question=f"Test Question {i}", answer=f"Answer {i}", categories="General")
        
        self.assertEqual(FAQ.objects.count(), 6)

        # 7th FAQ must raise ValidationError
        faq_7 = FAQ(question="7th Question", answer="7th Answer", categories="General")
        with self.assertRaises(ValidationError):
            faq_7.save()

        # Admin add permission must return False
        admin_obj = FAQAdmin(FAQ, AdminSite())
        self.assertFalse(admin_obj.has_add_permission(None))

    def test_user_terms(self):
        response = self.client.get(reverse('user_terms'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Terms")

    def test_unique_categories_extractor(self):
        cats = get_unique_categories(Skill.objects, "categories")
        self.assertIn("Backend", cats)
        self.assertIn("Core", cats)
        self.assertIn("Systems", cats)

    def test_contact_form_ajax_success(self):
        data = {
            "name": "Alex Carter",
            "email": "alex@example.com",
            "subject": "System Architecture Inquiry",
            "message": "Hello Roshan, I saw your work on DevMeet and would love to connect."
        }
        response = self.client.post(
            reverse('home'),
            data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
            REMOTE_ADDR='198.51.100.1'
        )
        self.assertEqual(response.status_code, 200)
        json_res = response.json()
        self.assertTrue(json_res.get('success'))
        self.assertTrue(ContactMessage.objects.filter(name="Alex Carter", ip_address='198.51.100.1').exists())

    def test_contact_form_missing_fields_validation(self):
        data = {
            "name": "",
            "email": "alex@example.com",
            "subject": "",
            "message": ""
        }
        response = self.client.post(
            reverse('home'),
            data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 400)
        json_res = response.json()
        self.assertFalse(json_res.get('success'))

    def test_contact_form_rate_limiting(self):
        ip = '203.0.113.42'
        # Seed submissions up to limit
        for i in range(10):
            ContactMessage.objects.create(
                name=f"User {i}",
                email=f"user{i}@example.com",
                subject="Spam test",
                message="Testing rate limit",
                ip_address=ip
            )

        with self.settings(DEBUG=False):
            response = self.client.post(
                reverse('home'),
                {
                    "name": "Spam Bot",
                    "email": "spam@example.com",
                    "subject": "Exceed Limit",
                    "message": "Blocked message"
                },
                HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                REMOTE_ADDR=ip
            )
            self.assertEqual(response.status_code, 429)
            json_res = response.json()
            self.assertFalse(json_res.get('success'))

    def test_resume_endpoints_without_file(self):
        # Empty DB for resumes
        Resume.objects.all().delete()
        res_view = self.client.get(reverse('resume'))
        self.assertEqual(res_view.status_code, 404)

        res_dl = self.client.get(reverse('download_resume'))
        self.assertEqual(res_dl.status_code, 404)

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/xml')
        self.assertContains(response, '<urlset')
        self.assertContains(response, 'devmeet-platform')
        self.assertContains(response, 'clean-architecture-principles-in-python')

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertContains(response, 'User-agent: *')
        self.assertContains(response, 'Sitemap:')
        self.assertContains(response, 'sitemap.xml')

    def test_custom_404_page(self):
        with self.settings(DEBUG=False):
            response = self.client.get('/non-existent-random-endpoint/')
            self.assertEqual(response.status_code, 404)
            self.assertContains(response, "404", status_code=404)
            self.assertContains(response, "Page Not Found", status_code=404)

    def test_custom_error_views_direct_render(self):
        from django.test import RequestFactory
        from app.views import custom_404_view, custom_500_view, custom_403_view, custom_400_view
        
        factory = RequestFactory()
        req = factory.get('/')
        
        # Test 404
        r404 = custom_404_view(req)
        self.assertEqual(r404.status_code, 404)
        
        # Test 500
        r500 = custom_500_view(req)
        self.assertEqual(r500.status_code, 500)
        
        # Test 403
        r403 = custom_403_view(req)
        self.assertEqual(r403.status_code, 403)
        
        # Test 400
        r400 = custom_400_view(req)
        self.assertEqual(r400.status_code, 400)

    def test_skill_icon_lookup_api(self):
        # Test lookup with empty name
        res_empty = self.client.get(reverse('skill_icon_lookup'))
        self.assertEqual(res_empty.status_code, 200)
        self.assertFalse(res_empty.json().get('found'))

        # Test lookup for a well-known skill (e.g. Python)
        res_python = self.client.get(reverse('skill_icon_lookup') + '?name=Python')
        self.assertEqual(res_python.status_code, 200)
        data = res_python.json()
        self.assertTrue(data.get('found'))
        self.assertIn('http', data.get('url'))

    def test_skill_auto_fetch_icon_on_creation(self):
        # Create a skill without providing an icon
        auto_skill = Skill.objects.create(name="Docker", level=88, status="Expert", categories="DevOps")
        self.assertIsNotNone(auto_skill.icon)
        self.assertTrue(bool(auto_skill.icon.name))
        self.assertTrue(auto_skill.icon.name.endswith('.svg'))

    def test_admin_login_page_renders_custom_template(self):
        response = self.client.get('/dash-admin/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Roshan's Desk")
        self.assertContains(response, "Sign In to Dashboard")

    def test_upload_settings_limits(self):
        from django.conf import settings
        self.assertEqual(settings.DATA_UPLOAD_MAX_MEMORY_SIZE, 100 * 1024 * 1024)
        self.assertEqual(settings.FILE_UPLOAD_MAX_MEMORY_SIZE, 50 * 1024 * 1024)
        self.assertEqual(settings.DATA_UPLOAD_MAX_NUMBER_FIELDS, 2500)

    def test_pagination_page_sizes(self):
        # Create 16 skills to test 15 per page
        for i in range(16):
            Skill.objects.create(name=f"TechSkill_{i}", level=70, status="Learning", categories="Test")
        res_skills = self.client.get(reverse('skill_list'))
        self.assertEqual(res_skills.status_code, 200)
        self.assertEqual(res_skills.context['page_obj'].paginator.per_page, 15)

        # Create 10 projects to test 9 per page
        for i in range(10):
            Project.objects.create(title=f"Test Project {i}", description="Test Description", categories="Test")
        res_projects = self.client.get(reverse('project_list'))
        self.assertEqual(res_projects.status_code, 200)
        self.assertEqual(res_projects.context['page_obj'].paginator.per_page, 9)

        # Create 10 blogs to test 9 per page
        for i in range(10):
            Blog.objects.create(title=f"Test Blog {i}", content="<p>Test content</p>", categories="Test", image="blogs/test.webp")
        res_blogs = self.client.get(reverse('blog_list'))
        self.assertEqual(res_blogs.status_code, 200)
        self.assertEqual(res_blogs.context['page_obj'].paginator.per_page, 9)

    def test_home_and_list_latest_first_ordering(self):
        newest_project = Project.objects.create(
            title="Brand Newest Project Alpha",
            categories="Web, AI",
            description="Created most recently"
        )
        response_home = self.client.get(reverse('home'))
        self.assertEqual(response_home.status_code, 200)
        # Check that the first project in context is the newest one
        home_projects = list(response_home.context['projects'])
        self.assertTrue(len(home_projects) > 0)
        self.assertEqual(home_projects[0].id, newest_project.id)

        response_list = self.client.get(reverse('project_list'))
        list_projects = list(response_list.context['page_obj'])
        self.assertEqual(list_projects[0].id, newest_project.id)


