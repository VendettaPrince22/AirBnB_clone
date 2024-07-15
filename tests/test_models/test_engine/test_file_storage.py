import unittest
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_all(self):
        storage = FileStorage()
        with open("file.json", 'r') as f:
            my_dict = json.load(f)
        self.assertEqual(len(storage.all()), len(my_dict))


if __name__ == "__main__":
    unittest.main()
