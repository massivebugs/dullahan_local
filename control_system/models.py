from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import json

# Create your models here.

class Device(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='device', null=True)
    name = models.CharField(default="My New Device", max_length=50)
    description = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    CONNECTION_TYPE_CHOICES = [
        ('BT', 'Bluetooth'),
    ]
    connection_type = models.CharField(
        max_length=2,
        choices=CONNECTION_TYPE_CHOICES,
        default='BT'
    )
    hostname = models.CharField(max_length=50, blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('get_device_control', kwargs={'device_id':self.id}) 

    def get_command_history(self):
        return json.loads(self.command_history)

class CommandHistory(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='history', null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    command = models.TextField(blank=True, null=True)
