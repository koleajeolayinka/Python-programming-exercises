import random

guess_random = random.randint(0, 100)
print("guess the magic number between1 - 100")
user_input = -1
while user_input != guess_random:
    user_input = int(input("Guess a number "))
    if user_input == guess_random:
        print("you are correct")
    elif user_input > guess_random:
        print("you are high")
    else:
        print("the number is low")
