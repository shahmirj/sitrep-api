"""
This file holds the definition of our ControllerBase

@author Shahmir Javaid
"""

from flask_restful import Resource

"""
This is our Base controller which holds the information required
for all controllers
"""
class IndexController(Resource):

  def get(self):
        return {'hello': 'david'}
