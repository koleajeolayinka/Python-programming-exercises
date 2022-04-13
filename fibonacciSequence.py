# fibonacci = input("enter a number: ")
# fibonacci = str(fibonacci)
# num = len(fibonacci)
# sum0 = int(fibonacci[0])
# sum1 = int(fibonacci[1])
# total = sum0 + sum1
#
# print(total)

 #Python 3: Fibonacci series up to n
def fib(n):
 a, b = 0, 1
 while a < n:
    print(a, end=' ')
    a, b = b, a+b
 print()
fib(1000000000000)