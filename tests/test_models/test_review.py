import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.new_review = Review()

    def test_place_id(self):
        self.assertEqual(self.new_review.place_id, "")

    def test_user_id(self):
        self.assertEqual(self.new_review.user_id, "")

    def test_text(self):
        self.assertEqual(self.new_review.text, "")


if __name__ == "__main__":
    unittest.main()
