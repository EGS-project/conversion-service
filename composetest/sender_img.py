import stomp
import time
from PIL import Image
import io
import subprocess
import base64
import xml.etree.ElementTree as ET

def prepare_message(filename,image): # "XML encoder" - incorrect naming but used for now
    
    with open(filename, 'rb') as f:
        image_data = f.read()

    img_b64data = base64.b64encode(image_data).decode('utf-8')

    root = ET.Element("image")

    name = ET.SubElement(root, "filename")
    name.text = filename

    b64_data = ET.SubElement(root, "b64_string")
    b64_data.text = img_b64data

    width_se = ET.SubElement(root, "width")
    width_se.text = str(image.size[0])

    height_se = ET.SubElement(root, "height")
    height_se.text = str(image.size[1])

    mode_se = ET.SubElement(root, "mode")
    mode_se.text = image.mode

    format_se = ET.SubElement(root, "format")
    format_se.text = image.format

    xml_string = ET.tostring(root, encoding='utf-8',xml_declaration=True)
    return xml_string

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error yes')
    def on_message(self, headers, message):
        print('received a message: message')

conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', MyListener())

conn.connect('admin', 'admin', wait=True)
queue_name = '/queue/test_img'

filename = '/home/alvaro/Desktop/Universidade/2ndSemestre/EGS/conversion-service/composetest/anemone.png'
img = Image.open(filename)
xml_string = prepare_message(filename,img)

try:
    conn.send(body=xml_string,destination='queue/test_img',headers={'filename': 'anemone.png'})
except KeyboardInterrupt:
    print('\nStopping...')
finally:
    conn.disconnect()
