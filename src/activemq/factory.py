import stomp
import stomp.connect as connect
import src.config as config

class ActiveMqConnectionFactory:
    
    @classmethod
    def create_connection(
        cls, 
        broker_host: str = config.ACTIVEMQ_HOST, 
        broker_port: int = int(config.ACTIVEMQ_PORT), 
        broker_username: str = config.ACTIVEMQ_USERNAME, 
        broker_password: str = config.ACTIVEMQ_PASSWORD, 
        listener: connect.ConnectionListener=None,
        ssl_active: bool=False
        ) -> connect.StompConnection11:
        conn = stomp.Connection(host_and_ports=[(broker_host, broker_port)])
        if listener:
            conn.set_listener(
                name='', 
                listener=listener
                )
        conn.connect(
            broker_username, 
            broker_password, 
            wait=True
        )
        
        return conn
