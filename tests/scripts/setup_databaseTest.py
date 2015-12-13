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
from app.scripts import setup_database

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
    self.mongo.get_client().drop_database(
      self.mongo.get_client().get_default_database()
    );

  """
  When I run postdeploy it creates a connection
  """
  def test_running_postdeploy_creates_structure(self):
    setup_database.main()
    collections = self.mongo.get_client()\
      .get_default_database().collection_names(include_system_collections=False)
    self.assertEqual(
      collections,
      [ "users", "orgs", "services" ]
    )
    self.assertEqual(3, len(collections))


if __name__ == '__main__':
    unittest.main()
