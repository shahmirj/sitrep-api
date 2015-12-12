"""
This class tests the Index Controller
"""

# Global imports
import unittest
import os
from pymongo import MongoClient
from pymongo.database import Database

# Local includes
from app.models.Mongo import Mongo

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class MongoTest(unittest.TestCase):

  """
  Set up a global instance of the controller
  """
  def setUp(self):
    Mongo.client = None;
    self.mongo = Mongo()

  """
  When I send a request to the controller it should return with a
  response
  """
  def test_mongo_returns_client(self):
    self.assertIsInstance(Mongo.get_client(), MongoClient)
    client  = Mongo.get_client()
    self.assertEqual(client.get_default_database().name, 'sitrep')

if __name__ == '__main__':
    unittest.main()
