"""
This file holds the definition of our ControllerBase

@author Shahmir Javaid
"""

from flask_restful import Resource, fields, marshal_with

from app.models.Org import Org

class OrgsController(Resource):
  """
  This is our Base controller which holds the information required
  for all controllers
  """

  resource_fields = {
      'name': fields.String,
      'services': fields.List(fields.String)
  }

  @classmethod
  @marshal_with(resource_fields)
  def get(cls):
    #if Org.objects(name='arkham').count() == 0:
    #  Org(name='arkham').save()
    """
    Simple GET call for /orgs/
    """
    orgs = []
    for org in Org.objects():
      orgs.append(org.to_mongo())
    return orgs
