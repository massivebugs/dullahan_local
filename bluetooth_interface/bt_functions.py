import bluetooth
from bluetooth.btcommon import BluetoothError

def search():
    try:
        message = "Searching for nearby BlueTooth devices..."
        print(message)

        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                                flush_cache=True, lookup_class=False)

        message = f"Found {len(nearby_devices)} devices"
        print(message)

        devices = {}

        for addr, name in nearby_devices:
            devices[name] = addr

        return devices
    except:
        print('Could not find any devices')
        return {}

def connect(bd_addr, port_num):
    try:
        print(f'Connecting to {bd_addr}')
        sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

        print('got sock instance')
        sock.connect((bd_addr, port_num))

        msg = f'Connected to {bd_addr}'
        print('returning sock')
        return (sock, msg)

    except BluetoothError as err:
        print(err)
        msg = 'Failed to connect to device'
        return (1, msg)

    except:
        return (1, 'An error has occured')

def send_serial(sock, message):
    try:
        print('sending message')
        sock.send(message)

        # TODO: Fix the message lag
        msg = sock.recv(1024)
        if len(msg) < 3:
            msg = 'Error with parsing message'
            raise Exception(msg)

        msg = msg.decode('utf-8')

    except BluetoothError as err:
        msg = err.msg

    except Exception as err:
        msg = err.msg

    finally:
        return msg
        

def close_connection(sock):
    try:
        sock.close()
        return 0
    except:
        return 1
