user_input = input("enter a number")
sum = 1
while sum <= 10:
    print(sum)
    sum += 1
    max_width = len(str(m[-1][-1])) + 1
    for i in m:
        i = [str(j).rjust(max_width) for j in i]
        print(''.join(i))