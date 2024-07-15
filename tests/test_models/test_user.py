import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_email(self):
        new_user = User()
        self.assertEqual(new_user.email, "")


if __name__ == "__main__":
    unittest.main()
