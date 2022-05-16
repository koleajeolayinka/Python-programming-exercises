# user_input = int(input("enter a number"))
# while user_input != 1:
#   if user_input % 2 != 0:
#     odd = user_input * 3 + 1
#     print(odd)
#     break
#
#   else:
#    odd = user_input / 2
#    print(odd)
#    break

n = 'tobi'  # n = 1221
# n = str(n)
print(n == n[::-1])
name = 'koleajeolayinkaoluwatobi'
print(len(name))
print(name * 3)

char = "spam" + '_' + "spam_"

print(char)
for i in range(11, 0, -1):
    print("*" * i)

for i in range(1, 11):
    print("*" * i)

for j in range(11, 0, -1):
    print("2" * j and "2" * j and "*" * i)

a_str = 'spam'
new_str = a_str[:1] + "l" + a_str[2:]
print((new_str))

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK...")
    audio = r.listen(source)
    print(r.recognize_google(audio))
