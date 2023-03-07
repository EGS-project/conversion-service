import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('Error received: "%s"' % message)

    def on_message(self, headers, message):
        print('Message received: "%s"' % message)

conn = stomp.Connection([('localhost', 61616)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'admin', wait=True)
conn.subscribe(destination='/queue/test', id=1, ack='auto')
print('Waiting for messages...')
while True:
    try:
        conn.consume()
    except KeyboardInterrupt:
        conn.disconnect()
        print('\nDisconnected from ActiveMQ')
        break