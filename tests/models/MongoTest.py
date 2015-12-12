"""
This class tests the Index Controller
"""

# Global imports
import unittest
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
    self.mongo = Mongo()

  """
  When I send a request to the controller it should return with a
  response
  """
  def test_mongo_returns_client(self):
    self.assertIsInstance(Mongo.get_client(), MongoClient);

  """
  When I ask for the database it should return me the database as
  loaded from configurations
  """
  def test_mongo_returns_database(self):
    self.assertIsInstance(Mongo.get_database(), Database);

if __name__ == '__main__':
    unittest.main()
