from django.shortcuts import render
from django.urls import reverse
from .models import Contact 
from .forms import ContactForm
 

def home_view(request): 
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
            return render(request, 'pages/home.html')
    else: 
        return render(request, 'pages/home.html')