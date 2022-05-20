def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class Account:
    def __init__(self, name):
        self.airtime = None
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:

            raise ValueError("AMOUNT CANNOT BE NEGATIVE")
        self.balance += amount

    def total_balance(self balance):

        

    def airtime(self, amount):
        self.airtime = amount

    




