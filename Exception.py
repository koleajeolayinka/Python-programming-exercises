def divide(a, b):
    if b == 0:
        raise ValueError("DENOMERATOR CAN NOT BE ZERO")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("ohh")
    return a / b

    # print(divide(2,5))


# print(divide(2,-1))
num = int(input("enter the numerator: "))
den = int(input("enter the numerator: "))
while True:
    try:
        print(divide(num, den))
        break
    except ValueError:
        print("Wrong value")
        num = int(input("enter the numerator: "))
        den = int(input("enter the denominator: "))
