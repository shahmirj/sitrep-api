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
    client = self.mongo.get_client()
    self.assertEqual(client.get_default_database().name, 'sitrep_testing')

  """
  When I call the get_db function I should get the default database
  """
  def test_mongo_get_database(self):
    self.assertIsInstance(self.mongo.get_db(), Database)
    self.assertEqual(self.mongo.get_db().name, 'sitrep_testing')

if __name__ == '__main__':
    unittest.main()
