import logging
from PIL import Image, UnidentifiedImageError
import io
import PIL.Image as Img

class Converter:
    supported_formats = ['JPEG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'PPM']

    @classmethod
    def convert(cls, data: bytes, format: str) -> bytes:
        if not data or format not in cls.supported_formats:
            return None
        
        byte_stream = io.BytesIO(data)
        try:
            img: Image = Image.open(byte_stream)
        except UnidentifiedImageError:
            return None

        buffer = io.BytesIO()
        if img.mode != 'RGB':
            if format == 'JPEG' or format == 'BMP' or format == 'TIFF':
                img = img.convert('RGB')

        img.save(buffer, format=format)
        
        return buffer.getvalue()
    