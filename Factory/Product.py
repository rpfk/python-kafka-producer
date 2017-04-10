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
