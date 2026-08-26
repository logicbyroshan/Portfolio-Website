import re
from django import template

register = template.Library()

@register.filter(name='is_video_link')
def is_video_link(url):
    if not url or not isinstance(url, str):
        return False
    return any(domain in url for domain in ['youtube.com', 'youtu.be', 'vimeo.com'])

@register.filter(name='youtube_embed')
def youtube_embed(url):
    if not url or not isinstance(url, str):
        return ""
    
    url = url.strip()
    
    # Check for youtube.com/watch?v=VIDEO_ID
    if 'youtube.com/watch' in url:
        match = re.search(r'[?&]v=([^&#]+)', url)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
            
    # Check for youtu.be/VIDEO_ID
    if 'youtu.be/' in url:
        match = re.search(r'youtu\.be/([^?&#]+)', url)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"

    # Check for youtube.com/embed/VIDEO_ID
    if 'youtube.com/embed/' in url:
        return url

    # Check for vimeo.com/VIDEO_ID
    if 'vimeo.com/' in url:
        match = re.search(r'vimeo\.com/(?:channels/(?:\w+/)?|groups/[^/]+/videos/|video/|)(\d+)', url)
        if match:
            return f"https://player.vimeo.com/video/{match.group(1)}"
            
    return url
