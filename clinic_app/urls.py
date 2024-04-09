from django.urls import path
from . import views

# URL patterns list for the 'clinic' app
urlpatterns = [
    # Define a URL pattern for the HomePageView view
    path('', views.HomePageView.as_view(), name='home'),    
]