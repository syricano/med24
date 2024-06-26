from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages  # Import the messages module
from .models import Message 
from django.http import HttpResponse


def contact_view(request):
    if request.method == "POST":
        contact = Message()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        
        # Create and save the message
        Message.objects.create(name=name, phone=phone, email=email, subject=subject)

        # Add a success message
        messages.success(request, 'Thanks for contacting us!')
        # Redirect back to the contact page
        return redirect('contact:contact')

    return render(request, 'contact.html')