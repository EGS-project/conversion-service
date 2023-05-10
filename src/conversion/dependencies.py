from src.activemq.dependencies import activemq_dispatcher
from src.conversion.listener import ConvertImageListener

convert_image_listener = ConvertImageListener(
    dispatcher=activemq_dispatcher
    )
