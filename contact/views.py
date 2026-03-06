from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import logging

from .forms import EnquiryForm
from .models import Enquiry

logger = logging.getLogger(__name__)


def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            # Capture IP
            x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
            enquiry.ip_address = (
                x_forwarded.split(',')[0] if x_forwarded
                else request.META.get('REMOTE_ADDR')
            )
            enquiry.save()
            _send_admin_notification(enquiry)
            _send_client_confirmation(enquiry)
            messages.success(
                request,
                f"Thank you {enquiry.first_name}! We've received your enquiry and will be in touch shortly."
            )
            return redirect('contact:success')
    else:
        form = EnquiryForm()

    return render(request, 'contact/contact.html', {'form': form})


def success(request):
    return render(request, 'contact/success.html')


# ── Email helpers ──────────────────────────────────────────────────────────────

def _send_admin_notification(enquiry: Enquiry):
    subject = f"New Enquiry – {enquiry.get_service_display()} from {enquiry.full_name}"
    html_body = render_to_string('contact/email/admin_notification.html', {'enquiry': enquiry})
    text_body = (
        f"New enquiry received\n\n"
        f"Name: {enquiry.full_name}\n"
        f"Phone: {enquiry.phone}\n"
        f"Email: {enquiry.email}\n"
        f"Service: {enquiry.get_service_display()}\n"
        f"Location: {enquiry.location}\n\n"
        f"Message:\n{enquiry.message}"
    )
    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
            reply_to=[enquiry.email] if enquiry.email else [],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()
    except Exception as exc:
        logger.error("Admin notification email failed: %s", exc)


def _send_client_confirmation(enquiry: Enquiry):
    if not enquiry.email:
        return
    subject = "We've received your enquiry – Light World Engineering"
    html_body = render_to_string('contact/email/client_confirmation.html', {
        'enquiry': enquiry,
        'company': settings.COMPANY,
    })
    text_body = (
        f"Hi {enquiry.first_name},\n\n"
        f"Thank you for reaching out to Light World Engineering!\n"
        f"We've received your enquiry for {enquiry.get_service_display()} "
        f"and will contact you on {enquiry.phone} shortly.\n\n"
        f"Call us any time: {settings.COMPANY['phone']}\n"
        f"Email: {settings.COMPANY['email']}\n\n"
        f"Everywhere to Anyone – Light World Engineering"
    )
    try:
        msg = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[enquiry.email],
        )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()
    except Exception as exc:
        logger.error("Client confirmation email failed: %s", exc)
