from django.urls import path
from .views import (
    device_index_view,
    device_control_view,
    device_create_view,
    device_delete_view,
    device_search_ajax,
)

urlpatterns = [
    path('', device_index_view, name='get_device_index'),
    path('control/<int:device_id>',device_control_view, name='get_device_control'),
    path('new/', device_create_view, name='get_device_new'),
    path('delete/<int:device_id>', device_delete_view, name='post_device_delete'),
    path('search/', device_search_ajax, name='ajax_search_device'),
]
