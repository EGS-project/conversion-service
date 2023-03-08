import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('Error received: "%s"' % message)

    def on_message(self, headers, message):
        print('Message received: "%s"' % message)

conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', MyListener())

conn.connect('admin', 'admin', wait=True)
conn.subscribe(destination='/queue/test', id=1, ack='auto')
print('Waiting for messages...')
