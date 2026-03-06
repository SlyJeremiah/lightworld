from django.contrib import admin
from django.utils.html import format_html
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'phone', 'email_link', 'service_badge',
        'location', 'status', 'created_at'
    ]
    list_filter = ['service', 'status', 'created_at']
    list_editable = ['status']
    search_fields = ['first_name', 'last_name', 'phone', 'email', 'location']
    readonly_fields = ['ip_address', 'created_at', 'updated_at']
    fieldsets = (
        ('Client Info', {
            'fields': ('first_name', 'last_name', 'phone', 'email')
        }),
        ('Enquiry Details', {
            'fields': ('service', 'location', 'message')
        }),
        ('Status & Notes', {
            'fields': ('status', 'notes')
        }),
        ('Meta', {
            'fields': ('ip_address', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def email_link(self, obj):
        if obj.email:
            return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
        return '–'
    email_link.short_description = 'Email'

    def service_badge(self, obj):
        return format_html(
            '<span style="font-size:12px;font-weight:600">{}</span>',
            obj.get_service_display()
        )
    service_badge.short_description = 'Service'