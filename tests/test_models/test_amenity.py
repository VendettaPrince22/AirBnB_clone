import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_ammenity = Amenity()

    def test_name(self):
        self.assertEqual(self.new_ammenity.name, "")


if __name__ == "__main__":
    unittest.main()
