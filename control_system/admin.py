from django.contrib import admin

# Register your models here.
from .models import Device, CommandHistory
admin.site.register(Device)
admin.site.register(CommandHistory)
