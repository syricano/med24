from . import views
from django.urls import path


app_name = 'contact_app'
# URL patterns list for the 'contact' app
urlpatterns = [
    # Define a URL pattern for the ContactUs view
    path('', views.contact_view, name='contact'),    
]