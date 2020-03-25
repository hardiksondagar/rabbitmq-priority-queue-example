import sys
import time
import pika

import common

if __name__ == '__main__':

    # default priority 0
    priority = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    channel = common.get_channel()
    queue_name = common.queue_name

    # publish with priority
    for i in range(5):
        message = 'message#{index}-with-priority{priority}'.format(
            index=i+1, priority=priority
        )
        channel.basic_publish(
            properties=pika.BasicProperties(priority=priority),
            exchange='',
            routing_key=queue_name,
            body=message
        )
        print("Published:", message)
        time.sleep(0.1)
