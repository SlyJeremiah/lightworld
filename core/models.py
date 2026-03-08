from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"{self.name} – {self.rating}★"


class GalleryImage(models.Model):
    SERVICE_CHOICES = [
        ('borehole', 'Borehole'),
        ('solar', 'Solar'),
        ('repair', 'Repair'),
        ('survey', 'Site Survey'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    video_url = models.URLField(blank=True, default='')
    media_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='other')
    caption = models.CharField(max_length=250, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title