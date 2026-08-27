"""
Skill Icon Auto-Fetcher Service
Fetches developer & technology icons automatically using a 3-tier fallback CDN architecture:
  - Tier 1: Devicon CDN (https://devicon.dev)
  - Tier 2: Simple Icons CDN (https://simpleicons.org)
  - Tier 3: Skill Icons CDN (https://github.com/tandpfun/skill-icons)
"""

import re
import logging
import urllib.request
import urllib.error
from django.core.files.base import ContentFile

logger = logging.getLogger(__name__)

# Common name normalization map for programming languages and developer tools
NAME_NORMALIZE_MAP = {
    # Languages & Frameworks
    "c++": "cplusplus",
    "c#": "csharp",
    ".net": "dot-net",
    "dotnet": "dot-net",
    "node.js": "nodejs",
    "node js": "nodejs",
    "node": "nodejs",
    "react.js": "react",
    "react js": "react",
    "react": "react",
    "react native": "react",
    "vue.js": "vuejs",
    "vue js": "vuejs",
    "vue": "vuejs",
    "angular.js": "angularjs",
    "angular": "angularjs",
    "next.js": "nextjs",
    "next js": "nextjs",
    "next": "nextjs",
    "express.js": "express",
    "express js": "express",
    "express": "express",
    "tailwind": "tailwindcss",
    "tailwind css": "tailwindcss",
    "tailwindcss": "tailwindcss",
    "bootstrap": "bootstrap",
    "bootstrap 5": "bootstrap",
    "django": "django",
    "django rest framework": "django",
    "drf": "django",
    "flask": "flask",
    "fastapi": "fastapi",
    "spring boot": "spring",
    "spring": "spring",
    "ruby on rails": "rails",
    "rails": "rails",
    "golang": "go",
    "go": "go",
    "rust": "rust",
    "python": "python",
    "javascript": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "ts": "typescript",
    "html": "html5",
    "html5": "html5",
    "css": "css3",
    "css3": "css3",
    "sass": "sass",
    "scss": "sass",
    "php": "php",
    "laravel": "laravel",
    "java": "java",
    "kotlin": "kotlin",
    "swift": "swift",
    "flutter": "flutter",
    "dart": "dart",
    "r": "r",
    "julia": "julia",
    "scala": "scala",
    
    # Databases & Storage
    "postgres": "postgresql",
    "postgresql": "postgresql",
    "mysql": "mysql",
    "mongodb": "mongodb",
    "mongo": "mongodb",
    "redis": "redis",
    "sqlite": "sqlite",
    "sqlite3": "sqlite",
    "cassandra": "cassandra",
    "mariadb": "mariadb",
    "couchdb": "couchdb",
    "firebase": "firebase",
    "supabase": "supabase",
    "neo4j": "neo4j",
    "elasticsearch": "elasticsearch",

    # Cloud & DevOps & OS
    "aws": "amazonwebservices",
    "amazon web services": "amazonwebservices",
    "azure": "azure",
    "microsoft azure": "azure",
    "gcp": "googlecloud",
    "google cloud": "googlecloud",
    "google cloud platform": "googlecloud",
    "docker": "docker",
    "kubernetes": "kubernetes",
    "k8s": "kubernetes",
    "git": "git",
    "github": "github",
    "gitlab": "gitlab",
    "bitbucket": "bitbucket",
    "linux": "linux",
    "ubuntu": "ubuntu",
    "debian": "debian",
    "centos": "centos",
    "redhat": "redhat",
    "arch linux": "archlinux",
    "nginx": "nginx",
    "apache": "apache",
    "jenkins": "jenkins",
    "ansible": "ansible",
    "terraform": "terraform",
    "prometheus": "prometheus",
    "grafana": "grafana",
    "postman": "postman",
    "jira": "jira",
    "confluence": "confluence",
    "figma": "figma",
    "photoshop": "photoshop",
    "illustrator": "illustrator",
    "canva": "canva",
    "celery": "celery",
    "kafka": "apachekafka",
    "rabbitmq": "rabbitmq",
    "graphql": "graphql",
}

def normalize_skill_name(raw_name: str) -> str:
    """Normalize raw skill name to a standard slug."""
    clean = raw_name.strip().lower()
    if clean in NAME_NORMALIZE_MAP:
        return NAME_NORMALIZE_MAP[clean]
    
    # Strip non-alphanumeric except dashes
    slug = re.sub(r'[^a-z0-9]+', '', clean)
    return slug

def query_icon_cdn(url: str, timeout: int = 4):
    """Safely query an icon CDN URL and return SVG bytes if valid."""
    try:
        req = urllib.request.Request(
            url, 
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status == 200:
                content = response.read()
                if b"<svg" in content or b"<?xml" in content:
                    return content
    except Exception as e:
        logger.debug(f"CDN query failed for {url}: {e}")
    return None

def fetch_skill_icon(skill_name: str):
    """
    Search 3-tier free icon libraries for a given skill name.
    
    Returns:
        tuple: (svg_content_bytes, cdn_source_name, direct_url) or (None, None, None)
    """
    if not skill_name or not skill_name.strip():
        return None, None, None

    raw_clean = skill_name.strip().lower()
    slug = normalize_skill_name(skill_name)
    slug_simple = re.sub(r'[^a-z0-9]+', '', raw_clean)

    candidate_slugs = list(dict.fromkeys([slug, slug_simple, raw_clean]))

    for s in candidate_slugs:
        # Tier 1: Devicon CDN (Original and Plain variations)
        devicon_variants = [
            f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{s}/{s}-original.svg",
            f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{s}/{s}-plain.svg",
            f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{s}/{s}-original-wordmark.svg",
        ]
        for url in devicon_variants:
            content = query_icon_cdn(url)
            if content:
                logger.info(f"Skill icon for '{skill_name}' found in Tier 1 (Devicon): {url}")
                return content, "Devicon", url

        # Tier 2: Simple Icons CDN
        simple_variants = [
            f"https://cdn.simpleicons.org/{s}",
            f"https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/{s}.svg",
        ]
        for url in simple_variants:
            content = query_icon_cdn(url)
            if content:
                logger.info(f"Skill icon for '{skill_name}' found in Tier 2 (SimpleIcons): {url}")
                return content, "SimpleIcons", url

        # Tier 3: Skill Icons CDN
        skill_variants = [
            f"https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/{s}.svg",
        ]
        for url in skill_variants:
            content = query_icon_cdn(url)
            if content:
                logger.info(f"Skill icon for '{skill_name}' found in Tier 3 (SkillIcons): {url}")
                return content, "SkillIcons", url

    logger.info(f"No free icon found across 3 tiers for skill '{skill_name}'.")
    return None, None, None

def auto_assign_skill_icon(skill_instance) -> bool:
    """
    If the skill does not already have an uploaded icon, auto-fetch from CDN and save.
    """
    if skill_instance.icon and skill_instance.icon.name:
        return False  # Already has user-provided icon

    content, source, url = fetch_skill_icon(skill_instance.name)
    if content:
        slug = normalize_skill_name(skill_instance.name)
        filename = f"{slug}.svg"
        skill_instance.icon.save(filename, ContentFile(content), save=False)
        return True
    return False
