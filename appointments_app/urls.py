from django.urls import path
from . import views

# URL patterns list for the 'clinic' app
urlpatterns = [
    # Define a URL pattern for the AppointmentView view
    path('', views.AppointmentView.as_view(), name='appointment'),    
]