import io
import pytest
import stomp
from src.conversion.message import ConvertImageMsg, ConvertImageReplyMsg
from src.activemq.dispatcher import ActivemqDispatcher
import src.config as config
import logging
from src.conversion.converter import Converter
from PIL import Image

@pytest.fixture()
def image_bytes_jpg_mock() -> bytes:
    with open('sample_images/raccoon.jpg', 'rb') as f:
        return f.read()


@pytest.fixture()
def target_format_mock():
    return 'PNG'

def test_convert_jpg_to_png(
    image_bytes_jpg_mock: bytes,
    target_format_mock: str
    ):
    assert isinstance(target_format_mock, str)
    assert isinstance(image_bytes_jpg_mock, bytes)
    
    converted_bytes = Converter.convert(
        data=image_bytes_jpg_mock,
        format=target_format_mock
        )
    assert isinstance(converted_bytes, bytes)
    
    pil_image = Image.open(io.BytesIO(converted_bytes))
    assert pil_image.format.lower() == 'png'
    
    with open('sample_images/output.png', "wb") as file:
        file.write(converted_bytes)
    
    x =-1
