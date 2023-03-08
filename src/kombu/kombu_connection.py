import kombu
import ssl


class KombuConnection:

  CONNECTION = None

  @classmethod
  def create_connection (cls, broker_url, broker_username, broker_password, ssl_active=False):

    # Create Connection String
    protocol = "amqp" + ("s" if ssl_active else "")
    connection_string = f"{protocol}://{broker_username}:{broker_password}@{broker_url}/"

    # Kombu Connection
    ssl_config = { 'cert_reqs': ssl.CERT_NONE } if ssl_active else False
    cls.CONNECTION = kombu.Connection(
      connection_string,
      heartbeat=4,
      ssl=ssl_config
    )

  @classmethod
  def get_exchange (cls, exchange_name):
    
    # Kombu Exchange
    return kombu.Exchange(
      name=exchange_name,
      type="direct",
    )

  @classmethod
  def get_queue (cls, exchange_name, queue_name):

    # Kombu Queues
    return [
      kombu.Queue(
        name=queue_name,
        exchange=cls.get_exchange(exchange_name)
      )
    ]

  @classmethod
  def get_producer (cls, exchange_name, queue_name):
    # Kombu Exchange
    kombu_exchange = cls.get_exchange(exchange_name)

    # Kombu Producer
    kombu_producer = kombu.Producer(
      exchange=kombu_exchange,
      channel=KombuConnection.CONNECTION.channel()
    )

    # Kombu Queue
    kombu_queue = kombu.Queue(
      name=queue_name,
      exchange=kombu_exchange
    )
    kombu_queue.maybe_bind(KombuConnection.CONNECTION)
    kombu_queue.declare()

    return kombu_producer