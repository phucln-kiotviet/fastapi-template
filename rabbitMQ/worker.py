import pika
import time
import sys
import os


def main():

    RABBITMQ_URL = 'localhost'
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(
        queue='task_queue',
        durable=True  # Make sure queue will survive a RabbitMQ node restart
    )

    def callback(channel, method, properties, body):
        print("[x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print("[x] Done")
        channel.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue',
                          on_message_callback=callback)

    print('[x] Waiting for message. To exit press CTRL+C: ')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
