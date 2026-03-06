from django.contrib import admin
from .models import Service, ServicePackage, BoreholeAddon


class PackageInline(admin.TabularInline):
    model = ServicePackage
    extra = 1
    fields = ['name', 'kva_label', 'base_price', 'labour_price', 'is_featured', 'is_active', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'price_label', 'is_active', 'order']
    list_filter = ['category', 'is_active']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PackageInline]


@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'base_price', 'labour_price', 'is_featured', 'is_active', 'order']
    list_filter = ['category', 'is_featured', 'is_active']
    list_editable = ['is_featured', 'is_active', 'order']


@admin.register(BoreholeAddon)
class BoreholeAddonAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_unit', 'unit', 'order']
    list_editable = ['order']
