import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_init(self):
        my_model = BaseModel()

        self.assertIsInstance(my_model, BaseModel)

if __name__ == "__main__":
    unittest.main()
