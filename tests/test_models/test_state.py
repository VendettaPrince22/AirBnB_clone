import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.new_state = State()

    def test_name(self):
        self.assertEqual(self.new_state.name, "")


if __name__ == "__main__":
    unittest.main()
