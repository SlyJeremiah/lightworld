from django.shortcuts import render, get_object_or_404
from .models import Service, ServicePackage, BoreholeAddon


def service_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    packages = service.packages.filter(is_active=True)
    return render(request, 'services/service_detail.html', {
        'service': service,
        'packages': packages,
    })


def solar_packages(request):
    packages = ServicePackage.objects.filter(
        category='solar', is_active=True
    ).order_by('base_price')
    return render(request, 'services/solar_packages.html', {'packages': packages})


def borehole_pricing(request):
    addons = BoreholeAddon.objects.all()
    return render(request, 'services/borehole_pricing.html', {'addons': addons})
