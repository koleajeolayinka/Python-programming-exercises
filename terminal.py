s = "This is the world of python"
wo = s.find('t')
print(wo)
print("I read the {1} textbook {1} times in {1} day".format(0, 1))
print("I read the {1} textbook {0} times in {1} day".format(5, 20))
smiley = "\U0001f600"
print(smiley)
for i in range(1, 21, 2):
    print(f"{smiley * i:^40}")
star = "*"
for i in range(1, 11):
    print(f"{star * i:<10}    {star * (11 - i):<10}   {star * (11 - i):>10}     {star * i:>10}")
for i in range(1, 11):
    print(f"{smiley * i:<10}    {smiley * (11 - i):<10}     {smiley * (11 - i):>10}     {smiley * i:<10}")
for index, letter in enumerate("hello world"):
    print(f"{letter} is in index {index}")
