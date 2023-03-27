import stomp
import stomp.connect as connect

class ActiveMqConnectionFactory:
    
    @classmethod
    def create_connection(
        cls, 
        broker_host: str, 
        broker_port: int, 
        broker_username: str, 
        broker_password: str, 
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
    