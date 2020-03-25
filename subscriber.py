import time

import common


if __name__ == '__main__':

    channel = common.get_channel()
    queue_name = common.queue_name

    # get messages
    while True:
        method_frame, header_frame, body = channel.basic_get(queue_name)
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
            print("Recevied:", body)
        time.sleep(0.1)
