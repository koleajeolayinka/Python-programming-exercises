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
        account1 = account.Account("tobi")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN:
        WHEN: when a deposit
        THEN: account balance should be reflected
        """
        account1 = account.Account("tobi")
        name = account1.name
        account1.deposit(200)
        self.assertEqual("tobi", name)
        self.assertEqual(200, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("tobi")
        account1.deposit(500)

        self.assertRaises(ValueError, account1.deposit, -1000)

        self.assertEqual(500, account1.balance)

    def test_that_account_can_load_airtime(self):
        account1 = account.Account("tobi")
        account1.balance(100)
        account1.airtime(200)
        account1.total_balance()
        self.assertEqual(200, account1.airtime)

    def test_account_can_transfer(self):
        account1 = account.Account("tobi")
        account1.balance(1000)
        account1.transfer(300)
        self.assertEqual(700, account1.currentBalance)

    # def test_account_can_withdraw(self)



if __name__ == '__main__':
    unittest.main()
