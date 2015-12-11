"""
This class tests the Index Controller
"""


# Global imports
import unittest
from flask import Request
from flask_restful import Resource

# Local includes
from app.controllers import IndexController
import server

"""
This class tests the ControllerBase by creating a mock from this
Base class
"""
class IndexControllerTest(unittest.TestCase):

  """
  Set up a global instance of the controller
  """
  def setUp(self):
    self.app = server.app.test_client()
    #self.controller = IndexController(Resource());

  """
  When I send a request to the controller it should return with a
  response
  """
  def test_controller_returns_response(self):
    self.assertEqual(self.app.get('/').data, '{"hello": "david"}')

if __name__ == '__main__':
    unittest.main()
