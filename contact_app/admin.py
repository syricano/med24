from django.contrib import admin
from .models import Administrator, Message, UserMessage

admin.site.register(Administrator)
admin.site.register(Message)
admin.site.register(UserMessage)
