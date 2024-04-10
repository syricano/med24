from django.shortcuts import render
from django.views.generic import ListView, TemplateView  
from .models import HomePage, AboutUs


# Define app's name
app_name = 'clinic_app'

class HomePageView(ListView):
    template_name = 'index.html'  # Specify the template name

    def get_queryset(self):
        return HomePage.objects.all()

class AboutUsView(ListView):
    template_name = 'about.html'  

    def get_queryset(self):
        return AboutUs.objects.all()