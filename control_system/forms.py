from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'name',
            'description',
            'connection_type',
            'hostname',
            'uuid',
            'password'
        ]
