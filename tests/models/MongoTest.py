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
    self.assertIsInstance(Mongo.get_client(), MongoClient);

  """
  Make sure the connection string by default is taken from the
  enviornment variable MONGOLAB_URI
  """
  def test_mongo_returns_client_using_env_vars(self):
    client  = Mongo.get_client()
    address = client.address
    self.assertEqual(address[0], '127.0.0.1')
    self.assertEqual(address[1], 27017)

if __name__ == '__main__':
    unittest.main()
