import threading
import time
from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def __init__(self, zk_hosts, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.zk_hosts = zk_hosts

    def run(self):
        producer = KafkaProducer(bootstrap_servers=self.zk_hosts)

        while True:
            producer.send('my-topic', b"test")
            producer.send('my-topic', b"\xc2Hola, mundo!")
            print('test')
            time.sleep(.1)


def daemon(zk_hosts):
    threads = [
        Producer(zk_hosts)
    ]

    for t in threads:
        t.start()

    time.sleep(10)
