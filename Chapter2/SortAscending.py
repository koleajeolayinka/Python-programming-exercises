# 2.15 (Sort in Ascending Order) Write a script that inputs three different floating-point
# numbers from the user. Display the numbers in increasing order. Recall that an if state-
# ment’s suite can contain more than one statement. Prove that your script works by run-
# ning it on all six possible orderings of the numbers. Does your script work with duplicate
# numbers? [This is challenging. In later chapters you’ll do this more conveniently and with
# many more numbers.]
firstNumber = input("ENTER YOUR FIRST NUMBER")
SecondNumber = input("ENTER YOUR SECOND NUMBER")
ThirdNumber = input("ENTER YOUR THIRD NUMBER")

if firstNumber <= SecondNumber and SecondNumber >= ThirdNumber:
    print(firstNumber,)
    print(ThirdNumber)
    print(SecondNumber)
elif firstNumber >= SecondNumber and SecondNumber <= ThirdNumber:
    print(ThirdNumber)
    print(SecondNumber)
    print(firstNumber)


