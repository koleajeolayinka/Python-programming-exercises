import math

print("WELCOME TO THE ULTIMATE CIRCLE CALCULATION")
print("KINDLY ENTER RADIUS")
radius = int(input())

print(" PRESS 1 TO CALCULATE CIRCLE DIAMETER\
\n PRESS 2 TO CALCULATE CIRCLE CIRCUMFERENCE\
\n PRESS 3 TO CALCULATE AREA OF A CIRCLE")
user_input = int(input())
if user_input == 1:
    diameter = 2 * radius
    print("SINCE YOU SUCCESSFULLY INPUT", radius, "AS RADIUS, THE DIAMETER OF CIRCLE  IS: ", diameter)
elif user_input == 2:
    circumference = 2 * math.pi * radius
    print("SINCE YOU SUCCESSFULLY INPUT", radius, "AS RADIUS, THE CIRCUMFERENCE OF CIRCLE  IS: ", circumference)

elif user_input == 3:
    area = math.pi * (radius ** 2)
    print("SINCE YOU SUCCESSFULLY INPUT", radius, "AS RADIUS, THE AREA OF CIRCLE  IS: ", area)
else:
    print("INCORRECT INPUT")



