import unittest

from person import Person

class TestAllowedToBuyAlcohol(unittest.TestCase):
    def setUp(self) -> None:
        self._person_ = Person()

    def test_age_too_low(self):
        self.assertEqual(True, _person_.allowed_to_buy_alcohol('',4.6))

    def test_age_allowed_to_buy(self):
        self.assertEqual(True, _person_.allowed_to_buy_alcohol('', 46.6))

if __name__=="__main__":
    unittest.main()
