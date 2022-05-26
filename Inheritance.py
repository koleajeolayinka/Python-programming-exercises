# class Animal:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         return "I speak"
#
#
# class Dog(Animal):
#     def __init__(self, name, type):
#         super().__init__(name)
#         self.type = type
#
#     pass
#
#
# class Cat(Animal):
#     def __init__(self, name, type_):
#         super().__init__(name)
#         self.type = type_
#
#     pass
#
#
# # class Bingo
#
# dog = Dog("Bingo", "local")
# cat = Cat("petty", "white")
#
# # bingo = Bingo("Bingo")
# print(dog.name, dog.type, dog.age)
# print(cat.name, cat.type)
# # print(dog.)
# help(dog)
#
# import abc
#
#
# class A(abc.ABC):
#
#     @abc.abstractmethod
#     def must_be_implement(self):
#         return
#
#
# class B(A):
#
#     def must_be_implement(self):
#         print("Hello")


class YourMoneyNoReachError(Exception):

    def __init__(self, message="") -> None:
        super().__init__(message)


raise YourMoneyNoReachError("Hello")
