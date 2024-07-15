import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.new_place = Place()

    def test_city_id(self):
        self.assertEqual(self.new_place.city_id, "")

    def test_user_id(self):
        self.assertEqual(self.new_place.user_id, "")

    def test_name(self):
        self.assertEqual(self.new_place.name, "")

    def test_description(self):
        self.assertEqual(self.new_place.description, "")

    def test_number_rooms(self):
        self.assertEqual(self.new_place.number_rooms, 0)

    def test_number_bathrooms(self):
        self.assertEqual(self.new_place.number_bathrooms, 0)

    def test_max_guest(self):
        self.assertEqual(self.new_place.max_guest, 0)

    def test_price_by_night(self):
        self.assertEqual(self.new_place.price_by_night, 0)

    def test_latitude(self):
        self.assertEqual(self.new_place.latitude, 0.0)

    def test_longitude(self):
        self.assertEqual(self.new_place.longitude, 0)

    def test_amenity_ids(self):
        self.assertEqual(self.new_place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
