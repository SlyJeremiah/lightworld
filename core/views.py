from django.shortcuts import render
from core.models import Testimonial, GalleryImage
from services.models import ServicePackage
from contact.models import Enquiry


def home(request):
    testimonials = Testimonial.objects.filter(is_featured=True)[:6]
    gallery = GalleryImage.objects.filter(is_active=True)[:8]
    solar_packages = ServicePackage.objects.filter(
        category='solar', is_active=True
    ).order_by('base_price')
    stats = {
        'projects': Enquiry.objects.filter(status='completed').count() or '100+',
        'years': 5,
        'provinces': 10,
    }
    return render(request, 'core/home.html', {
        'testimonials': testimonials,
        'gallery': gallery,
        'solar_packages': solar_packages,
        'stats': stats,
    })


def about(request):
    return render(request, 'core/about.html')


def gallery_view(request):
    category = request.GET.get('cat', '')
    images = GalleryImage.objects.filter(is_active=True)
    if category:
        images = images.filter(category=category)
    
    # debug
    import logging
    logger = logging.getLogger(__name__)
    logger.error("GALLERY DEBUG: total=%s active=%s cat=%s", 
        GalleryImage.objects.count(),
        GalleryImage.objects.filter(is_active=True).count(),
        category
    )
    
    return render(request, 'core/gallery.html', {
        'images': images,
        'active_cat': category,
    })