from django.shortcuts import render
from django.views.generic import ListView
from .models import Appointment


# Define app's name
app_name = 'appointments_app'

class AppointmentView(ListView):
    template_name = 'appointment.html'  # Specify the template name

    def get_queryset(self):
        return Appointment.objects.all()