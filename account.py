def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class Account:
    def __init__(self, name):
        self.balance = 0
        self.transfer = self.transfer
        self.currentBalance = self.balance - self.transfer
        self.airtime = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("AMOUNT CANNOT BE NEGATIVE")
        self.balance += amount

    def transfer(self, transfer):
        self.balance += transfer
