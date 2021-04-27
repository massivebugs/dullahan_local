# Dependencies 
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from datetime import datetime
import json

# Models
from .models import Device, CommandHistory

# Error classes
from django.core.exceptions import ObjectDoesNotExist

class CommandConsumer(WebsocketConsumer):
    """ Channels consumer class for interfacing with websockets and the client."""

    def connect(self):
        # TODO: Read more about consumer scopes
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.device_group_name = 'command_%s' % self.device_id
        device = Device.objects.get(id=self.device_id)

        # Connect to device by passing bt-process info and group_name
        async_to_sync(self.channel_layer.send)('bt-process', {
            'type': 'bt_connect',
            'group_name': self.device_group_name,
            'uuid': device.uuid,
            'device' : device.id,
            }
        )

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.device_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.device_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        device_id = text_data_json['device']

        # Send message to device
        async_to_sync(self.channel_layer.send)('bt-process', {
            'type': 'bt_send_serial',
            'device': device_id,
            'message': message,
            }
        )

        # Send message to device group
        async_to_sync(self.channel_layer.group_send)(
            self.device_group_name,
            {
                'type': 'command_message',
                'device': device_id,
                'message': message,
            }
        )

    # Receive from group and send to websocket
    def command_message(self, event):
        message = event['message']
        device_id = event['device']
        
        # Appends command to command history
        device = Device.objects.get(id=device_id)
        new_history = CommandHistory(device=device, command=message )
        new_history.save()

        command_history = {}
        all_history = device.history.all()
        for command in all_history:
            command_history[command.timestamp.strftime('%H:%M:%S')] = command.command + '\n'


        # Sends back whole command history
        self.send(text_data=json.dumps({
            'message': command_history,
            'device': device_id
        }))
