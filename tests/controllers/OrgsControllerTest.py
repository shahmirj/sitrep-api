"""
This class tests the OrgsController
"""

# Global imports
import unittest
import os
from flask import Request, json
from flask_restful import Resource
from mongoengine import *
from mongoengine.connection import get_connection

# Local includes
from app.models.Mongo import Mongo
from app.models.Org import Org
import server

"""
This class will test OrgsController
"""
class OrgsControllerTest(unittest.TestCase):


  def setUp(self):
    """
    Set up a global instance of the controller
    """
    self.app = server.app.test_client()

  def tearDown(self):
    """
    Tear down the database
    """
    con = get_connection();
    con.drop_database(con.get_default_database())

  def test_orgs_returns_empty_array_on_default(self):
    """
    When I send a request to the controller it should return with a
    response
    """
    data = json.loads(self.app.get('/orgs/').data)
    self.assertEqual(data, [])

  def test_orgs_returns_org(self):
    """
    When I have two organisations they should be returned
    """
    Org(name='arkham').save()
    Org(name='batcave').save()
    data = json.loads(self.app.get('/orgs/').data)
    self.assertEqual(len(data), 2)

    self.assertEqual(data[0]['name'], 'arkham');
    self.assertEqual(data[1]['name'], 'batcave');

if __name__ == '__main__':
    unittest.main()
