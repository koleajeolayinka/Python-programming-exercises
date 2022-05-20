import unittest
from . import playground


class PlaygroundTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("i run before")

    def tearDown(self) -> None:
        print("I run after")

    def test_something1(self):
        print("i am running on my own-> 1 ")

    def test_something2(self):
        print("i am running on my own -> 2")
if __name__ == '__main__':
    unittest.main()
