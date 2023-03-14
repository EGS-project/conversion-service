import stomp
from PIL import Image
import io
import subprocess
import time
import os
import xml.etree.ElementTree as ET
import base64


def parse_message(message):
    print("parse_message called")
    root = ET.fromstring(message.body)

    print("getting  xml elements")
    filename = root.find("filename").text
    b64_data = root.find("b64_string").text
    width =root.find("width").text
    height =root.find("height").text
    mode =root.find("mode").text
    format =root.find("format").text


    image_data = base64.b64decode(b64_data.encode('utf-8'))
    #image = Image.frombytes(mode,(width,height),image_data)

    print("decoded image data and returning")
    return image_data


class ImageListener(object):
    def __init__(self):
        super().__init__()

    def on_message(self, message):
        print("on message called")
        image_data = parse_message(message)
        image = Image.open(io.BytesIO(image_data))
        image.show()
        print("parsed and printed message")

class Transport(object):
    def __init__(self, conn):
        self.conn = conn

    def notify(self, frame):
        if self.listener is not None:
            self.listener.on_message(frame.headers, frame.body)


conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', ImageListener())

conn.connect('admin', 'admin', wait=True)


conn.subscribe(destination='queue/test_img', id=1, ack='auto')
print("suubscribed")
while True:
    pass
conn.disconnect()

def on_message(self, headers, message):
    print('received a message "%s"' % message)
    # Extract base64 encoded image data from message
    img_b64data = message

    # Decode base64 string to get back original binary image data
    image_data = base64.b64decode(img_b64data.encode('utf-8'))
    
    # Process image_data as needed
    # ...
