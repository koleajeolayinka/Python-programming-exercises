def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        self.balance += amount




