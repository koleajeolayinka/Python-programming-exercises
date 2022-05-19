class Player(object):
    wine = input(int())

    def __init__(self, nameless: str, age: int, wine: int) -> None:
        self.name = nameless
        self.age = age
        self.wine = wine


player1 = Player("timmy", 45, wine)
print(player1.name)
print(player1.age)
print(player1.wine)
