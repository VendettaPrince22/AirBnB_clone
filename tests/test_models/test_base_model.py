import unittest
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.my_model, BaseModel)

    def test_save(self):
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, self.my_model.created_at)
        model_id = "BaseModel." + str(self.my_model.id)
        with open("file.json", 'r') as f:
            my_dict = json.load(f)
            self.assertIn(model_id, my_dict)

    def test_to_dict(self):
        my_dict = self.my_model.__dict__
        for key in my_dict.keys():
            self.assertIn(key, self.my_model.to_dict())


if __name__ == "__main__":
    unittest.main()
