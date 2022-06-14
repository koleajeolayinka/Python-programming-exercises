print("WELCOME TO FIVE DIGIT SEPERATOR")
Digit = int(input("PLEASE KINDLY ENTER FIVE DIGIT TO SEPARATE EACH DIGIT: "))
digit0 = Digit / 10000
# math.(digit0)
digit1 = int(Digit % 10000) / 1000
digit2 = (Digit % 1000) / 100
digit3 = (Digit % 100) / 10
digit4 = (Digit % 10)
print(f"{digit0}   {digit1}   {digit2}   {digit3}   {digit4}")
