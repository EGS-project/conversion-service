from PIL import Image, UnidentifiedImageError
import io

class Converter:
    supported_formats = ['PNG', 'JPEG']

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
        print(img.mode)
        if img.mode != 'RGB':
            if format == 'JPEG' or format == 'BMP' or format == 'TIFF':
                img = img.convert('RGB')
        img.save(buffer, format=format)
        
        return buffer.getvalue()
    