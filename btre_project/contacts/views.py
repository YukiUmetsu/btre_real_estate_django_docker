from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
import os

def contact(request):
    if request.method != 'POST':
        return render(request, 'listings.html')

    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
    contact.save()

    send_mail(
        'Inquary for '+listing,
        message,
        os.environ.get("EMAIL_HOST_USER"),
        [realtor_email],
        fail_silently=False,
    )
    messages.success(request, 'Your request has been submitted!')

    return redirect('/listings/'+listing_id)