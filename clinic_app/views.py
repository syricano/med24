from django.shortcuts import render
from django.views.generic import ListView
from .models import HomePage


# Define app's name
app_name = 'clinic_app'

class HomePageView(ListView):
    template_name = 'index.html'  # Specify the template name

    def get_queryset(self):
        return HomePage.objects.all()