import pika


queue_name = 'priority-queue'
max_priority = 10


def get_channel():
    # connect and get channel
    parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    # declare queue with max priority
    channel.queue_declare(
        queue=queue_name, arguments={"x-max-priority": max_priority}
    )
    return channel
