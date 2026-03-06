from django.conf import settings


def site_settings(request):
    """Injects company info and GA ID into every template."""
    return {
        'COMPANY': settings.COMPANY,
        'GA_ID': settings.GOOGLE_ANALYTICS_ID,
    }
