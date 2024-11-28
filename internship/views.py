
from django.shortcuts import render, redirect
from .models import UserRegistration
from django.core.mail import send_mail
from django.db import IntegrityError
from django.http import FileResponse
from django.conf import settings
import os

def download_database(request):
    if not request.user.is_staff:  # Restrict access to staff users
        return HttpResponseForbidden("You are not authorized to access this resource.")
    
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    if os.path.exists(db_path):
        return FileResponse(open(db_path, 'rb'), as_attachment=True, filename='db.sqlite3')
    else:
        return HttpResponseNotFound("Database file not found.")


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        domain = request.POST['domain']
        phone = request.POST['phone']
        try:
            # Save the user if the email doesn't exist
            UserRegistration.objects.create(name=name, email=email, domain=domain, phone=phone)
        except IntegrityError:
            # Handle duplicate email error
            return render(request, 'register.html', {
                'error': 'Email is already registered.Please use different email.'
            })
        # Send confirmation email
        send_mail(
                subject='Registration Successful',
                message=f'Hello {name},\n\nThank you for registering with codebytes! Our team will contact you shortly.',
                from_email='sibiyon2004@gmail.com',  # Replace with your email
                recipient_list=[email],
                fail_silently=False,
        )
        return redirect('success')
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def home(request):
    return render(request, 'home.html')
