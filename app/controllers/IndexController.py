"""
This file holds the definition of our ControllerBase

@author Shahmir Javaid
"""

from flask_restful import Resource


class IndexController(Resource):
  """
  This is our Base controller which holds the information required
  for all controllers
  """

  @classmethod
  def get(cls):
    """
    Simple GET call for /
    """
    return {'hello': 'david'}
