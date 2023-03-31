import pika
import sys
import os


def main():

    RABBITMQ_URL = 'localhost'
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(channel, method, properties, body):
        print("[x] Received %r" % body)

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print('[x] Waiting for message. To exit press CTRL+C: ')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exixt(0)
        except SystemExit:
            os.exit(0)
