# RabbitMQ Priority Message Example
This example will show how to publish and consume messages with priority.

### Dependencies
- RabbitMQ (>=3.5.0)
- Python 3.6
- Pika


#### 1. Publish messages with priority=0 (no priority)
```
$ python publisher.py 0
Published: message#1-with-priority0
Published: message#2-with-priority0
Published: message#3-with-priority0
Published: message#4-with-priority0
Published: message#5-with-priority0
```

#### 2. Publish messages with priority=10
```
$ python publisher.py 10
Published: message#1-with-priority10
Published: message#2-with-priority10
Published: message#3-with-priority10
Published: message#4-with-priority10
Published: message#5-with-priority10

```


#### 3. Get messages
```
$ python subscriber.py
Recevied: b'message#1-with-priority10'
Recevied: b'message#2-with-priority10'
Recevied: b'message#3-with-priority10'
Recevied: b'message#4-with-priority10'
Recevied: b'message#5-with-priority10'
Recevied: b'message#1-with-priority0'
Recevied: b'message#2-with-priority0'
Recevied: b'message#3-with-priority0'
Recevied: b'message#4-with-priority0'
Recevied: b'message#5-with-priority0'
```

In output we can see that messages with priority=10 consumed first even if it was published later.