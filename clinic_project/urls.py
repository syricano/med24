from django.contrib import admin
from django.urls import path,include
from clinic_app import views


urlpatterns = [
     # Admin site URLs
    path('admin/', admin.site.urls, name = "admin"),

    # Include URLs from the 'clinic_app' app
    path('', include("clinic_app.urls"), name = "clinic"),

    # Include URLs from the 'appointments_app' app
    path('appointment/', include("appointments_app.urls"), name = "appointment"),

    # Include URLs from the 'contact_app' app
    path('contact/', include("contact_app.urls"), name = "contact"),

    
]
