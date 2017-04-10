import importlib
import threading
import time
from numpy.random import choice
from faker import Faker
from bisect import bisect


class Factory(threading.Thread):
    daemon = True

    def __init__(self, assignment, producer, *args, **kwargs):
        super(Factory, self).__init__(*args, **kwargs)
        self.assignment = assignment
        self.producer = producer
        self.faker = Faker()
        self.products = self.create_products(assignment)
        self.production_rate = [int(s) for s in assignment['production_rate'].keys()]
        self.topic_mapping = [int(s) for s in assignment['topic_mapping'].keys()]

    @staticmethod
    def get_product(module_name, class_name):

        # load the module, will raise ImportError if module cannot be loaded
        m = importlib.import_module(module_name)

        # get the class, will raise AttributeError if class cannot be found
        c = getattr(m, class_name)

        return c

    def create_products(self, assignment):
        products = []
        for product in assignment['products']:
            products.append(self.get_product('Factory.Product', product))
        return products

    def run(self):

        start = time.time()
        while True:
            run_time = time.time() - start

            # get the production rate as defined in the factory assignment
            rate = self.assignment['production_rate'][str(self.production_rate[bisect(self.production_rate, run_time) - 1])]

            # get the send mapping as defined in the factory assignment
            topics = self.assignment['topic_mapping'][str(self.topic_mapping[bisect(self.topic_mapping, run_time) - 1])]

            # get the product to deliver
            product = choice(self.products, 1, p=self.assignment['product_weights'])[0]

            # deliver the product
            self.deliver(product(self.faker), topics)

            # for debugging
            print time.time()

            # determine the time to next delivery based on the production rate defined in the factory assignment
            time.sleep(1 / float(rate) - (run_time % (1 / float(rate))))

    def deliver(self, product, topic_mapping):
        for index, map_topic in enumerate(topic_mapping):
            if map_topic:
                # for debugging
                print self.assignment['topics'][index], product.key, product.value

                # send the product as message over Kafka
                self.producer.send(self.assignment['topics'][index], key=product.key, value=product.value)
