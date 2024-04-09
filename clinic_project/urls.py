from django.contrib import admin
from django.urls import path,include
from clinic_app import views


urlpatterns = [
     # Admin site URLs
    path('admin/', admin.site.urls, name = "admin"),

    # Include URLs from the 'clinic' app
    path('', include("clinic_app.urls"), name = "clinic"),
]
