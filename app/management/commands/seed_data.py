from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Project, ProjectImage, Feature, Learning, Blog, Skill, Experience, FAQ, Resume
import datetime

class Command(BaseCommand):
    help = "Seeds demo data for Roshan's portfolio"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding portfolio data..."))

        # Superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@roshandamor.site", "admin123")
            self.stdout.write(self.style.SUCCESS("Created superuser 'admin' with password 'admin123'"))

        # Resume
        if not Resume.objects.exists():
            resume = Resume.objects.create(file="resumes/Roshan_Damor_Resume1.pdf")
            self.stdout.write(self.style.SUCCESS(f"Created resume: {resume}"))

        # Skills
        skills_data = [
            {"name": "Python", "icon": "skills/icons/Python.webp", "level": 95, "status": "Expert", "categories": "Backend, Programming", "description": "Core language for backend systems, automation, and data processing.", "resource_links": "https://www.youtube.com/watch?v=_uQrJ0TkZlc,https://docs.python.org/"},
            {"name": "Django", "icon": "skills/icons/Django.webp", "level": 92, "status": "Expert", "categories": "Backend, Full-Stack, Web", "description": "High-level web framework for secure, scalable full-stack applications.", "resource_links": "https://www.youtube.com/watch?v=F5mRW0jo-U4,https://docs.djangoproject.com/"},
            {"name": "React-JS", "icon": "skills/icons/React-JS.webp", "level": 85, "status": "Expert", "categories": "Frontend, JavaScript", "description": "Modern component-driven declarative UI development.", "resource_links": "https://www.youtube.com/watch?v=bMknfKXIFA8,https://react.dev/"},
            {"name": "Next-JS", "icon": "skills/icons/Next-JS.webp", "level": 84, "status": "Expert", "categories": "Frontend, Full-Stack", "description": "Production React framework with SSR and App Router.", "resource_links": "https://nextjs.org/docs"},
            {"name": "PostgreSQL", "icon": "skills/icons/PostGreSQL.webp", "level": 88, "status": "Expert", "categories": "Database, Backend", "description": "Advanced relational database management, indexing, and complex queries.", "resource_links": "https://www.postgresql.org/docs/"},
            {"name": "Docker", "icon": "skills/icons/Docker.webp", "level": 80, "status": "Average", "categories": "DevOps, Cloud", "description": "Containerization and streamlined microservice deployment workflows.", "resource_links": "https://www.docker.com/"},
            {"name": "Redis", "icon": "skills/icons/Redis.webp", "level": 82, "status": "Expert", "categories": "Database, Caching, Backend", "description": "In-memory data store for caching, session stores, and real-time queues.", "resource_links": "https://redis.io/"},
            {"name": "Rest-API", "icon": "skills/icons/Rest-API.webp", "level": 95, "status": "Expert", "categories": "Backend, Architecture", "description": "RESTful API design, authentication (JWT/OAuth), and documentation.", "resource_links": "https://www.django-rest-framework.org/"},
            {"name": "MongoDB", "icon": "skills/icons/MongoDB.webp", "level": 78, "status": "Average", "categories": "Database, NoSQL", "description": "Document database for high-throughput flexible schema data.", "resource_links": "https://www.mongodb.com/"},
            {"name": "Tailwind", "icon": "skills/icons/Tailwind.webp", "level": 90, "status": "Expert", "categories": "Frontend, CSS", "description": "Utility-first CSS framework for rapid UI styling.", "resource_links": "https://tailwindcss.com/"},
            {"name": "AWS", "icon": "skills/icons/aws.webp", "level": 75, "status": "Learning", "categories": "Cloud, DevOps", "description": "Cloud infrastructure (EC2, S3, RDS, Lambda) for scalable apps.", "resource_links": "https://aws.amazon.com/"},
            {"name": "PyTorch", "icon": "skills/icons/Pytorch.webp", "level": 76, "status": "Learning", "categories": "AI/ML, Data Science", "description": "Deep learning and neural network experimentation.", "resource_links": "https://pytorch.org/"},
        ]

        created_skills = {}
        for s in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=s["name"],
                defaults={
                    "icon": s["icon"],
                    "level": s["level"],
                    "status": s["status"],
                    "categories": s["categories"],
                    "description": s["description"],
                    "certificate": "skills/certificates/Roshan_Portfolio_2024_March.pdf",
                    "resource_links": s["resource_links"],
                }
            )
            created_skills[s["name"]] = skill

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(created_skills)} skills"))

        # Projects
        if not Project.objects.exists():
            p1 = Project.objects.create(
                title="DevMeet - Developer Community & Real-time Platform",
                categories="Full-Stack, Web App",
                tags="Django, Python, WebSockets, React, PostgreSQL",
                description="A modern full-stack developer community platform featuring real-time messaging, portfolio showcasing, code sharing, and collaborative developer discovery.",
                problem_statement="Developers often struggle to find collaborators for niche tech stacks across disparate, non-interactive channels.",
                solution="Built a unified web platform with real-time matchmaking, live chat rooms, and automated GitHub repository synchronization.",
                impact="Connected 1,500+ active developers with average response times under 10 minutes.",
                github_link="https://github.com/logicbyroshan/devmeet-portfolio",
                live_link="https://roshandamor.site"
            )
            p1.skills.set([created_skills["Python"], created_skills["Django"], created_skills["React-JS"], created_skills["PostgreSQL"]])
            ProjectImage.objects.create(project=p1, image="projects/images/ac767d7240af0cfbeece4c47393cd923.webp")
            ProjectImage.objects.create(project=p1, image="projects/images/project_1.webp")
            Feature.objects.create(project=p1, title="Real-Time Chat & Rooms", description="Instant messaging powered by Django Channels & WebSockets.", image="projects/features/solution.webp")
            Feature.objects.create(project=p1, title="Dynamic Portfolio Hub", description="Showcase projects with interactive rich media previews.", image="projects/features/features.webp")
            Learning.objects.create(project=p1, paragraph="Mastered asynchronous ASGI architecture and WebSocket channel layers at scale.")
            Learning.objects.create(project=p1, paragraph="Optimized relational query access patterns using Django prefetch_related.")

            p2 = Project.objects.create(
                title="AI-Powered Code Analytics Engine",
                categories="AI/ML, Backend",
                tags="Python, AI/ML, Django REST, Docker",
                description="An automated static analysis and AI-driven code review platform optimizing Python & Django applications for security, performance, and best practices.",
                problem_statement="Manual code reviews frequently miss subtle database query bottlenecks (N+1 queries) and architectural anti-patterns.",
                solution="Engineered an AST-driven analysis pipeline combined with intelligent LLM prompts to flag vulnerabilities before pull requests merge.",
                impact="Reduced pull request review cycle times by 45% across participating development teams.",
                github_link="https://github.com/logicbyroshan/devmeet-portfolio",
                live_link="https://roshandamor.site"
            )
            p2.skills.set([created_skills["Python"], created_skills["Rest-API"], created_skills["Docker"], created_skills["PyTorch"]])
            ProjectImage.objects.create(project=p2, image="projects/images/project_3.webp")
            Feature.objects.create(project=p2, title="AST Code Parser", description="Deep syntactic analysis targeting query inefficiencies and security loopholes.", image="projects/features/meteorite.webp")
            Learning.objects.create(project=p2, paragraph="Gained deep insights into Python Abstract Syntax Trees (AST) and token-efficient AI workflows.")

            p3 = Project.objects.create(
                title="Cloud-Native E-Commerce Platform",
                categories="Full-Stack, Cloud",
                tags="Django, Redis, Stripe, Celery, PostgreSQL",
                description="High-concurrency microservices e-commerce application with automated inventory sync, Redis caching, and Stripe payment webhook processing.",
                problem_statement="Monolithic retail backends experienced significant degradation and race conditions during high-volume flash sales.",
                solution="Architected an asynchronous event-driven order processing pipeline with Redis locking and Celery distributed workers.",
                impact="Successfully handled 10,000+ peak requests per minute with zero dropped orders or double-spends.",
                github_link="https://github.com/logicbyroshan/devmeet-portfolio",
                live_link="https://roshandamor.site"
            )
            p3.skills.set([created_skills["Django"], created_skills["Redis"], created_skills["PostgreSQL"], created_skills["AWS"]])
            ProjectImage.objects.create(project=p3, image="projects/images/original-09dfdc662ec2d17e0abbca78c7a5074a.webp")
            Feature.objects.create(project=p3, title="Asynchronous Checkout Queue", description="Distributed worker-based cart reservation and payment settlement.", image="projects/features/book.webp")
            Learning.objects.create(project=p3, paragraph="Implemented robust idempotent webhook handlers and distributed Redis locking patterns.")

            self.stdout.write(self.style.SUCCESS("Seeded 3 featured projects with images, features, and learnings"))

        # Experiences
        if not Experience.objects.exists():
            Experience.objects.create(
                title="Senior Full-Stack Developer @ Tech Innovations",
                image="experience/Google.webp",
                start_date=datetime.date(2024, 1, 1),
                end_date=None,
                categories="Full-Stack, Leadership",
                description="Architecting enterprise web solutions using Django, Next.js, and cloud-native services. Mentoring team of engineers and spearheading code quality standards."
            )
            Experience.objects.create(
                title="Backend Python Developer @ CloudSphere Labs",
                image="experience/Amazon.webp",
                start_date=datetime.date(2022, 6, 1),
                end_date=datetime.date(2023, 12, 31),
                categories="Backend, Cloud",
                description="Engineered high-performance RESTful APIs, optimized complex database queries, and implemented a multi-tier Redis caching layer resulting in a 40% latency drop."
            )
            Experience.objects.create(
                title="Software Engineering Intern @ CodeCraft Studio",
                image="experience/Infosys.webp",
                start_date=datetime.date(2021, 8, 1),
                end_date=datetime.date(2022, 5, 31),
                categories="Web Development",
                description="Contributed to full-stack features, designed responsive UI components, and implemented automated unit & integration testing suites."
            )
            self.stdout.write(self.style.SUCCESS("Seeded 3 experiences"))

        # Blogs
        if not Blog.objects.exists():
            Blog.objects.create(
                title="Mastering Django ORM: Advanced Query Optimization & Performance Tips",
                categories="Django, Python, Performance",
                image="blogs/dell-8pb7Hq539Zw-unsplash.webp",
                content="""<h2>Understanding the N+1 Query Problem in Django</h2>
<p>When building scalable web applications with Django, database efficiency is often the deciding factor between a snappy user experience and sluggish performance. One of the most common pitfalls developers encounter is the <strong>N+1 query problem</strong>.</p>

<h3>Using <code>select_related</code> and <code>prefetch_related</code></h3>
<p>Django provides two powerful methods to eliminate unnecessary queries:</p>
<ul>
    <li><strong><code>select_related()</code></strong>: Works on <code>ForeignKey</code> and <code>OneToOneField</code> by performing an SQL <code>JOIN</code> in the database query.</li>
    <li><strong><code>prefetch_related()</code></strong>: Works on <code>ManyToManyField</code> and reverse foreign keys by executing a batch lookup in Python.</li>
</ul>

<pre><code># Example:
projects = Project.objects.select_related('author').prefetch_related('skills', 'images')
for project in projects:
    print(project.title, project.author.name)
</code></pre>

<h3>Database Indexing and Only/Defer</h3>
<p>Add <code>db_index=True</code> on fields used frequently in <code>filter()</code> and <code>order_by()</code> clauses. Use <code>.only()</code> or <code>.defer()</code> when loading records with large text or binary payloads.</p>
"""
            )

            Blog.objects.create(
                title="Building Resilient Real-Time Systems with WebSockets & Django Channels",
                categories="WebSockets, Backend, Architecture",
                image="blogs/onur-binay-O2-EZNGZIyk-unsplash.webp",
                content="""<h2>Real-Time Communication in Modern Web Apps</h2>
<p>From collaborative whiteboards to live notification feeds and chat systems, modern users demand real-time interactivity. Django Channels extends Django from a traditional HTTP-only request-response framework into a full ASGI-compliant asynchronous engine.</p>

<h3>Channel Layers with Redis</h3>
<p>A Channel Layer allows different instances of your application to communicate with each other over Redis pub/sub. When a user sends a message, it is broadcast across channel groups instantly.</p>

<pre><code>async def receive_json(self, content):
    room_group_name = f"chat_{content['room_id']}"
    await self.channel_layer.group_send(
        room_group_name,
        {
            "type": "chat_message",
            "message": content["message"]
        }
    )
</code></pre>
"""
            )

            Blog.objects.create(
                title="Clean Architecture Principles for Modern Full-Stack Python Applications",
                categories="Architecture, Best Practices",
                image="blogs/dell-LXI5kqCdEcE-unsplash.webp",
                content="""<h2>Why Clean Architecture Matters</h2>
<p>As applications grow in complexity, keeping business logic cleanly decoupled from framework internals (such as Django views and models) becomes essential for maintainability and testability.</p>

<h3>Key Layers in Clean Architecture:</h3>
<ol>
    <li><strong>Domain Entities:</strong> Core data structures and business rules.</li>
    <li><strong>Use Cases / Service Layer:</strong> Orchestration of business workflows.</li>
    <li><strong>Adapters & Gateways:</strong> Database ORMs, third-party APIs, and external storage.</li>
</ol>
<p>By enforcing clear dependency boundaries, swapping out third-party services or writing unit tests becomes seamless.</p>
"""
            )
            self.stdout.write(self.style.SUCCESS("Seeded 3 blogs"))

        # FAQs
        if not FAQ.objects.exists():
            FAQ.objects.create(
                question="What technologies and frameworks do you specialize in?",
                answer="I specialize in Python, Django, Django REST Framework, React, Next.js, PostgreSQL, Docker, Redis, and modern full-stack web architecture.",
                categories="General, Skills"
            )
            FAQ.objects.create(
                question="Are you available for freelance projects or full-time roles?",
                answer="Yes! I am actively open to high-impact full-time engineering roles, consulting engagements, and select contract projects. Feel free to reach out via the contact form!",
                categories="Hiring, Collaboration"
            )
            FAQ.objects.create(
                question="How do you approach application performance and database optimization?",
                answer="I prioritize clean query design, prefetching (select_related & prefetch_related), strategic indexing, Redis caching, and automated profiling to maintain sub-second response times.",
                categories="Engineering, Performance"
            )
            FAQ.objects.create(
                question="Can you help migrate legacy projects to modern tech stacks?",
                answer="Absolutely. I have experience refactoring legacy codebases into scalable, well-tested, containerized architectures with zero downtime.",
                categories="Consulting, Architecture"
            )
            self.stdout.write(self.style.SUCCESS("Seeded 4 FAQs"))

        self.stdout.write(self.style.SUCCESS("\n Portfolio database successfully seeded!"))
