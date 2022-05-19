# import speech_recognition as sr
#
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("SPEAK...")
#     print()
#     audio = r.listen(source)
#     print(r.recognize_google(audio))
# print(f"""
#
# PRESS ->> OPEN ACCOUNT
#       PRESS ->> TO LOGIN TO ACCOUNT
#      """)
# UserInput = int(input("ENTER YOUR PROMPT HERE"))
# if UserInput == 1:
#     print("OPEN  ACCOUNT")
# elif UserInput == 2:
#     print("LOGIN TO ACCOUNT")
file_obj = open("../venv/file.txt", mode="r+")
for line in file_obj.readline():
    for word in line.split(" "):
        print(word)
print(file_obj.readline())

file_obj.close()

# file_obj = open("file.txt", mode="r")
# print(file_obj.readline())
# # print("my world is not complete without you", file=file_obj)
# # print("my world is not complete without you", file=file_obj)
# # file_obj.close()
# with open('readme.txt', 'w') as f:
#     f.write('readme')
# f = open(path_to_file, mode)
# f.write('\n')
# f.writelines('\n')
# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'w') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')
# with open('readme.txt') as f:
#     lines = f.readlines()
# open(path_to_file, mode)
# f = open('the-zen-of-python.txt', 'r')
# f.close()
# with open(path_to_file) as f:
#     contents = f.readlines()

import json

config_dict = {
    "name": "adeola",
    "age": 18,
    1: "Birthday",
    "hobby": [1, 2, 3, 4],
    "bool": True

}
with open("../venv/config.json", mode="w") as file_obj:
    json.dump(config_dict, file_obj, indent=4, separators=(",", ":"))
    # for word in line.split(" "):
    #    print(word)
