from django.db import models


class ServiceChoice(models.TextChoices):
    SURVEY = 'survey', 'Site Survey ($80)'
    DRILLING = 'drilling', 'Borehole Drilling'
    INSTALL_ELECTRIC = 'install_electric', 'Borehole Installation – Electric ($1,900)'
    INSTALL_SOLAR = 'install_solar', 'Borehole Installation – Solar ($2,000)'
    SOLAR_1KVA = 'solar_1kva', 'Solar System – 1KVA ($650)'
    SOLAR_3KVA = 'solar_3kva', 'Solar System – 3KVA ($850)'
    SOLAR_6KVA = 'solar_6kva', 'Solar System – 6.2KVA ($1,500)'
    SOLAR_10KVA = 'solar_10kva', 'Solar System – 10KVA ($3,150)'
    REPAIR = 'repair', 'Borehole Repairs / Flushing'
    PUMP_FISHOUT = 'pump_fishout', 'Pump Fishout'
    ASSESSMENT = 'assessment', 'Assessment'
    OTHER = 'other', 'Other'


class StatusChoice(models.TextChoices):
    NEW = 'new', 'New'
    IN_PROGRESS = 'in_progress', 'In Progress'
    QUOTED = 'quoted', 'Quoted'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'


class Enquiry(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    service = models.CharField(max_length=30, choices=ServiceChoice.choices)
    location = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default='new')
    notes = models.TextField(blank=True, help_text='Internal notes')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.first_name} {self.last_name} – {self.get_service_display()} ({self.created_at.date()})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
