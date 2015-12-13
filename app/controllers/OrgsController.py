"""
This file holds the definition of our ControllerBase

@author Shahmir Javaid
"""

from flask_restful import Resource

from app.models.Org import Org
from bson import json_util
import json

class OrgsController(Resource):
  """
  This is our Base controller which holds the information required
  for all controllers
  """

  @classmethod
  def get(cls):
    """
    Simple GET call for /orgs/
    """
    orgs = []
    for org in Org.objects():
      orgs.append(org.to_mongo().to_dict())
    return orgs;
