import xml.etree.ElementTree as ET
import base64
from PIL import Image

def parse_message(message):
    root = ET.fromstring(message.body)

    filename = root.find("filename").text
    b64_data = root.find("b64_string").text
    width =root.find("width").text
    height =root.find("height").text
    mode =root.find("mode").text
    format =root.find("format").text

    return base64.b64decode(b64_data.encode('utf-8'))

def prepare_message(filename):  # use MIME for image messaging, MIME object goes inside XML message
    image = Image.open(filename)
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

    return ET.tostring(root, encoding='utf-8', xml_declaration=True)
