from django.contrib import admin
from .models import CustomUser, Name

admin.site.register(CustomUser)
admin.site.register(Name)