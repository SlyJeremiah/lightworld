from django.db import models
from django.utils.text import slugify


class ServiceCategory(models.TextChoices):
    SURVEY = 'survey', 'Site Survey'
    BOREHOLE = 'borehole', 'Borehole Drilling'
    INSTALLATION = 'installation', 'Borehole Installation'
    SOLAR = 'solar', 'Solar System'
    REPAIR = 'repair', 'Repairs & Maintenance'
    ASSESSMENT = 'assessment', 'Assessment'


class Service(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=ServiceCategory.choices)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(max_length=10, default='⚙️', help_text='Emoji icon')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_label = models.CharField(max_length=60, blank=True, help_text='e.g. "from $160" or "call for price"')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServicePackage(models.Model):
    """Specific priced packages, e.g. 1KVA Solar, 3KVA Solar."""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='packages')
    category = models.CharField(max_length=20, choices=ServiceCategory.choices, default='solar')
    name = models.CharField(max_length=100)           # e.g. "1KVA Solar Package"
    kva_label = models.CharField(max_length=20, blank=True)  # e.g. "1KVA"
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    labour_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    features = models.TextField(help_text='One feature per line')
    powers = models.TextField(blank=True, help_text='What appliances it can power')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'base_price']

    def get_features_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]

    def get_powers_list(self):
        return [p.strip() for p in self.powers.split('·') if p.strip()]

    def __str__(self):
        return self.name


class BoreholeAddon(models.Model):
    """Additional borehole pricing line items."""
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=30, default='per meter')
    icon = models.CharField(max_length=10, default='🔩')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} – ${self.price_per_unit}/{self.unit}"
