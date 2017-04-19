import json
import random


class Product(object):
    def __init__(self, faker):
        self.faker = faker
        self.key = self.key()
        self.value = self.value()

    def key(self):
        return 0

    def value(self):
        return 0

    def type(self):
        return self.__class__.__name__


class Text(Product):
    def key(self):
        return 'text'

    def value(self):
        return self.faker.text()


class Address(Product):
    def key(self):
        return 'address'

    def value(self):
        return self.faker.address()


class Name(Product):
    def key(self):
        return 'name'

    def value(self):
        return self.faker.name()


class Json(Product):
    def key(self):
        return 'json'

    def value(self):
        value = random.random() * 100

        return json.dumps([
            {'value_1': int(value), 'value_2': 'integer'},
            {'value_1': str(value), 'value_3': 'string'},
            {'value_1': value, 'value_4': 'float'}
        ])


class Person(Product):
    def key(self):
        return 'person'

    def value(self):
        return json.dumps({
            'name': self.faker.name(),
            'address': self.faker.address()
        })
