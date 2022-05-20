import unittest
from . import playground


class PlaygroundTest(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        print("i run before")

    def tearDownClass(self) -> None:
        print("I run after")


if __name__ == '__main__':
    unittest.main()
