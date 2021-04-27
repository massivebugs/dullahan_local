from channels.generic.websocket import SyncConsumer
from asgiref.sync import async_to_sync
from bluetooth_interface import bt_functions
from time import sleep

class BTConsumer(SyncConsumer):
    """
    A consumer instance for managing Bluetooth devices.
    
    This consumer instance contains all of the necessary methods to
    interact with Bluetooth devices in the background. This enables
    channels to maintain connection with many consumer instances at
    the same time without blocking HTTP and WebSockets interaction.

    """

    def bt_connect(self, message):
            # Remembers group name so that it has access to the current group and channels
            # TODO: Modify self.device_group_name so that it can hold multiple group names
            self.device_group_name = message['group_name']
            self.sock = {}

            # TODO: Assign port number dynamically
            self.port_num = 1

            # Get bt sock connection instance
            sock, msg = bt_functions.connect(message['uuid'], self.port_num)

            # Hold sock instance
            if sock != 1: 
                self.sock = {message['device']:[sock, self.port_num]}

            # Message results to group
            async_to_sync(self.channel_layer.group_send)(
                    self.device_group_name,
                    {
                        'type': 'command_message',
                        'device': message['device'],
                        'message': msg,
                        }
                    )

    def bt_listen(self, message):
        # TODO: Implement this!
        while(True):
            sleep(1)
            print('listen message here!')
            print(message)


    def bt_send_serial(self, event):
        """Looks up device's id and sends message to it's sock instance"""
        device_id = int(event['device'])
        message = event['message']

        if device_id in self.sock.keys():
            result = bt_functions.send_serial(self.sock[device_id][0], message)
            async_to_sync(self.channel_layer.group_send)(
                    self.device_group_name,
                    {
                        'type': 'command_message',
                        'device': device_id,
                        'message': result,
                        }
                    )

    def disconnect(self, message):
        result = bt_functions.close_connection()
        self.sock.pop(message['device'], None)
