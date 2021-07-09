from django.shortcuts import render
from .models import Contact 
from .forms import ContactForm
from django.contrib import messages  

def home_view(request): 
    form = ContactForm()
    return render(request, 'pages/home.html', {'form': form})

def homeform_view(request): 
    form = ContactForm(request.POST)
    if form.is_valid(): 
        form.save()
        messages.success(request, 'Contact form submitted!')
    
    return render(request, 'pages/home_form.html', {'form': form})