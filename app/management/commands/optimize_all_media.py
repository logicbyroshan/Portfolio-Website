from django.core.management.base import BaseCommand
import os
from PIL import Image
from io import BytesIO

class Command(BaseCommand):
    help = "Compress and convert all images in media/ and app/static/images/ to high-quality WebP"

    def handle(self, *args, **options):
        directories = [
            os.path.join("app", "static", "images"),
            "media"
        ]
        
        total_saved = 0
        file_count = 0

        for target_dir in directories:
            if not os.path.exists(target_dir):
                continue

            for root, _, files in os.walk(target_dir):
                for file in files:
                    ext = file.split('.')[-1].lower()
                    if ext in ['webp', 'png', 'jpg', 'jpeg']:
                        filepath = os.path.join(root, file)
                        original_size = os.path.getsize(filepath)

                        try:
                            with Image.open(filepath) as img:
                                is_icon = "icon" in root.lower() or "icons" in root.lower() or "skills" in root.lower()
                                
                                if is_icon:
                                    max_size = (300, 300)
                                    quality = 85
                                else:
                                    max_size = (1600, 1200)
                                    quality = 82

                                # Only process if large or not webp or oversized
                                if original_size > 100 * 1024 or ext != 'webp' or img.width > max_size[0] or img.height > max_size[1]:
                                    if img.mode in ('RGBA', 'P') and ext not in ['png', 'webp']:
                                        img = img.convert('RGB')
                                    
                                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                                    
                                    # Target path: always .webp
                                    webp_path = os.path.splitext(filepath)[0] + '.webp'
                                    
                                    temp_output = BytesIO()
                                    img.save(temp_output, format='WEBP', quality=quality, optimize=True)
                                    compressed_data = temp_output.getvalue()
                                    
                                    # Only replace if size is reduced or converted from non-webp
                                    if len(compressed_data) < original_size or ext != 'webp':
                                        with open(webp_path, 'wb') as f:
                                            f.write(compressed_data)
                                            
                                        if webp_path != filepath and os.path.exists(filepath):
                                            os.remove(filepath)
                                            
                                        saved = original_size - len(compressed_data)
                                        total_saved += max(0, saved)
                                        file_count += 1
                                        self.stdout.write(f"Optimized: {file} ({original_size // 1024} KB -> {len(compressed_data) // 1024} KB)")
                        except Exception as e:
                            self.stdout.write(self.style.WARNING(f"Could not process {filepath}: {e}"))

        mb_saved = total_saved / (1024 * 1024)
        self.stdout.write(self.style.SUCCESS(f"\nDone! Optimized {file_count} images. Total storage saved: {mb_saved:.2f} MB!"))
