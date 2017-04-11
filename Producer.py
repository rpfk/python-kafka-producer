import json
import time
from kafka import KafkaProducer
from Factory.Factory import Factory


class Producer(object):
    def __init__(self, kafka_address, assignment):
        self.assignment = json.loads(assignment)
        self.producer = 'producer'
        self.producer = KafkaProducer(bootstrap_servers=kafka_address,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      key_serializer=str.encode)
        self.factories = self.create_factories(self.assignment, self.producer)
        for factory in self.factories:
            factory.start()

        time.sleep(self.assignment['time'])

    @staticmethod
    def create_factories(assignments, producer):
        factories = []
        for assignment in assignments['factories']:
            factories.append(Factory(assignment, producer))
        return factories
