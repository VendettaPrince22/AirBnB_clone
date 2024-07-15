import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.new_city = City()

    def test_state_id(self):
        self.assertEqual(self.new_city.state_id, "")

    def test_name(self):
        self.assertEqual(self.new_city.name, "")


if __name__ == "__main__":
    unittest.main()
