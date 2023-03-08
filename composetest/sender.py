import stomp
import time

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', MyListener())

conn.connect('admin', 'admin', wait=True)
queue_name = '/queue/test'

try:
    while True:
        message = input('Enter message to send (or Ctrl-C to exit): ')
        conn.send(body=message, destination=queue_name)
        print('Sent message: "%s"' % message)
except KeyboardInterrupt:
    print('\nStopping...')
finally:
    conn.disconnect()
