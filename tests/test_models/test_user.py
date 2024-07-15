import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User()

    def test_email(self):
        self.assertEqual(self.new_user.email, "")

    def test_password(self):
        self.assertEqual(self.new_user.password, "")

    def test_first_name(self):
        self.assertEqual(self.new_user.first_name, "")

    def test_last_name(self):
        self.assertEqual(self.new_user.last_name, "")


if __name__ == "__main__":
    unittest.main()
