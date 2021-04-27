# Dependencies
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

# Custom dependencies
from bluetooth_interface import bt_functions as bt

# Models and ModelForms
from .models import Device
from .forms import DeviceForm

# Error classes
from django.core.exceptions import ObjectDoesNotExist
from .error_classes import CommandError


@login_required
def device_index_view(req):
    """Returns HTTP response of index template with user's devices"""

    try:
        queryset = req.user.device.all()
        context = {
            'object_list': queryset,
        }
        return render(req, 'index.html', context)
    except ObjectDoesNotExist:
        return Http404('Failed to retrieve devices')

@login_required
def device_control_view(req, *args, **kwargs):
    """Returns HTTP response of device specific control_interface template."""

    try:
        queryset = req.user.device.all()
        device_id = kwargs['device_id']
        selected_device = Device.objects.get(id=device_id)

        context = {
            'object_list': queryset,
            'selected_device': selected_device
        }
        return render(req, 'control_interface.html', context)
    except ObjectDoesNotExist:
        return Http404('Failed to retrieve devices')


@login_required
def device_create_view(req, *args, **kwargs):
    """Returns HTTP response of new device template"""

    form = DeviceForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            current_device = form.save()
            # Save user to model instance
            current_device.user = req.user
            current_device.save()
            # Reset the form
            form = DeviceForm()
            return HttpResponseRedirect(reverse('get_device_index'))
    else:
        context = {
            'form': form
        }
    return render(req, 'new.html', context)

@login_required
def device_search_ajax(req):
    """Returns JSON response of BlueTooth devices's Hostname and UUID"""

    try:
        if req.method == "GET":
            nearby_devices = json.dumps(bt.search())
            return JsonResponse({'nearby_devices':nearby_devices}, status=200)
        else:
            return JsonResponse({"error": ""}, status=400)
    except:
        # TODO: Error handling for BluetoothError
        return JsonResponse({"error": ""}, status=400)

@login_required
def device_delete_view(req, device_id):
    """Deletes object from models"""
    
    # TODO:Make it into a POST request handler, not GET
    device = get_object_or_404(Device, id=device_id)
    device.delete()
    return HttpResponseRedirect('/devices')
