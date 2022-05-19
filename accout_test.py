import unittest
import account


# from . import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        result = account.add(2, 3)
        self.assertEqual(5, result)

    def test_sub(self):
        self.assertEqual(5, account.sub(7, 2))


class Account_sub(unittest.TestCase):
    def test_that_can_sub(self):
        sub = account.sub(10, 5)
        self.assertEqual(5, sub)


class Account_Test(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account()

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN:
        WHEN:
        THEN:
        """



if __name__ == '__main__':
    unittest.main()
