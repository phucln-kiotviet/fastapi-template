import pika


RABBITMQ_URL = 'localhost'
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',  # will detail in part 3: https://www.rabbitmq.com/tutorials/tutorial-three-python.html
                      routing_key='hello',
                      body='Hello World!'
                      )
print(" [x] Sent 'Hello World!'")

connection.close()
