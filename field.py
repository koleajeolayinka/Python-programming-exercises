# try:
#     print("life is good")
#     # print(1 / 0)# Zero division error
#     # print([1,2,3][4])# index error
#     print("after life")
#
# except ZeroDivisionError as e:
#     print("zeroError", e)
# except IndexError as e:
#     print("index error", e)
# else:
#     print("I run only when there is no error")
# finally:
#     print("i run every, time")
class Player:
    name = "Yakuza"


Player1 = Player()
Player2 = Player()

print(Player1)
# Player1.name = "Ronaldo"
print(Player2)
print(Player1.name)
print(Player2.name)

