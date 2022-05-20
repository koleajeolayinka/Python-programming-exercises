import unittest
import shopping

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


class shopping_voucher(unittest.TestCase):
    def test_shopping_can_be_created(self):
        shopping1 = shopping.Basket()
        basket = shopping.BasketVoucher()
        b1 =



if __name__ == '__main__':
    unittest.main()
