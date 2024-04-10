from django.urls import path
from .views import HomePageView, AboutUsView

# URL patterns list for the 'clinic' app
urlpatterns = [
    # Define a URL pattern for the HomePageView view
    path('', HomePageView.as_view(), name='home'),
    
    # Define a URL pattern for the AboutUsView view
    path('about/', AboutUsView.as_view(), name='about'),     
]