class Playground:
    def __init__(self, age):
        self._age = age
        # self._name = f"{} {}"

    @property
    def age(self):
        print("am setting name")
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("AGE CANNOT BE NEGATIVE")
        self._age = age

    @age.deleter
    def age(self):
        print("DELETING AGE...")


p1 = Playground(1)
print(p1.age)
