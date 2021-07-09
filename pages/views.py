from django.shortcuts import render
from .models import Contact 
from .forms import ContactForm
from django.contrib import messages  

def home_view(request): 
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Contact form submitted!')
    else: 
        form = ContactForm()
    
    return render(request, 'pages/home.html', {'form': form})