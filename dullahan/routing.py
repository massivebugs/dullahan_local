from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from django.urls import path
#import control_system.routing
from control_system.consumers import CommandConsumer
from bluetooth_interface.consumers import BTConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('devices/control/<int:device_id>', CommandConsumer),
            ])
    ),
    'channel': ChannelNameRouter({
        'bt-process': BTConsumer,
    })
})
