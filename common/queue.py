import pika
import json
import logging

LOGGER = logging.getLogger(__name__)

class Queue(object):
  def __init__(self, url, **kwargs):
    self.queue = kwargs.get('queue', '')
    self.exchange = kwargs.get('exchange', '')
    self.key = kwargs.get('key', '')
    self.url = url
    LOGGER.debug('Opening connection to KVS %s', self.url)
    self.connection = pika.BlockingConnection(pika.URLParameters(self.url))
    self.channel = self.connection.channel()
#    self.channel.exchange_declare(exchange=self.exchange, durable=True)
#    self.channel.queue_declare(queue=self.queue, durable=True)
#    self.channel.queue_bind(queue=self.queue, exchange=self.exchange)

  def send_message(self, payload):
    message = json.dumps(payload)
    LOGGER.debug('Publishing message to %s with key %s',
      self.exchange, self.key
    )
    self.channel.basic_publish(
      exchange=self.exchange, routing_key=self.key, body=message,
      properties=pika.BasicProperties(
        content_type='application/json',
        delivery_mode=1
      )
    )
    self.connection.close()
