import sys
import pika

RABBITMQ_URL = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message
                      )

print(" [x] Sent %r" % message)
