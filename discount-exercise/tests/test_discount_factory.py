import unittest

from discount_factory import DiscountFactory


class DiscountFactoryTests(unittest.TestCase):
    def test_underage_student_discount(self):
        strategy = DiscountFactory.get_discount_strategy(17, True, False)
        self.assertEqual(strategy.discount_rate, 0.05)

    def test_underage_student_worker_discount(self):
        strategy = DiscountFactory.get_discount_strategy(17, True, True)
        self.assertEqual(strategy.discount_rate, 0.08)

    def test_adult_worker_student_discount(self):
        strategy = DiscountFactory.get_discount_strategy(30, True, True)
        self.assertEqual(strategy.discount_rate, 0.15)

    def test_no_discount_when_not_eligible(self):
        strategy = DiscountFactory.get_discount_strategy(25, False, False)
        self.assertEqual(strategy.discount_rate, 0.0)

    def test_old_discount(self):
        strategy = DiscountFactory.get_discount_strategy(70, False, False)
        self.assertEqual(strategy.discount_rate, 0.10)


if __name__ == "__main__":
    unittest.main()
