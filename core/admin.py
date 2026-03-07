from django.contrib import admin
from .models import Testimonial, GalleryImage


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured']
    list_editable = ['is_featured']
    search_fields = ['name', 'message']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'media_type', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    list_filter = ['media_type', 'is_active']
    search_fields = ['title', 'caption']