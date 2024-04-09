from django.contrib import admin
from .models import Appointment, Doctor, Administrator, Therapy, Reminder


admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(Administrator)
admin.site.register(Therapy)
admin.site.register(Reminder)