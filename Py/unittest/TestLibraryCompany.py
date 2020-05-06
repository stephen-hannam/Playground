import unittest

from Company import get_country

class TestLibraryCompany(unittest.TestCase):
    def test_allow_country(self):
        country = get_country(iso_code='DK')
        self.assertEqual(True, country[0])
        self.assertEqual(dict, type(country[1]))

    def test_disallow_country(self):
        country = get_country(iso_code='DA')
        self.assertEqual(False, country[0])
        self.assertEqual(None, country[1])

    def test_raise_country_TypeError(self):
        with self.assertRaises(TypeError):
            get_country()
            get_country(iso_code=12)

    def test_raise_country_ValueError(self):
        with self.assertRaises(ValueError):
            get_country(iso_code='Denmark')
            get_country(iso_code='D')
            get_country(iso_code='')

if __name__=="__main__":
    unittest.main()
