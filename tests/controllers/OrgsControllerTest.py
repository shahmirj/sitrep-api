"""
This class tests the OrgsController
"""

# Global imports
import unittest
from flask import Request, json
from flask_restful import Resource
from mongoengine import *

# Local includes
from app.models.Org import Org
import server

"""
This class will test OrgsController
"""
class OrgsControllerTest(unittest.TestCase):

  """
  Set up a global instance of the controller
  """
  def setUp(self):
    self.app = server.app.test_client()
    connect('sitrep', host='mongomock://localhost')


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

if __name__ == '__main__':
    unittest.main()
