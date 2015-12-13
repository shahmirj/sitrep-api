from mongoengine import *
import datetime

from app.models.Service import Service

class Org(Document):
  """
  This class is the ORM for the collection of orgs
  """

  name = StringField(max_length=50, required=True, unique=True)
  date_modified = DateTimeField(default=datetime.datetime.now)
  services = ListField(ReferenceField(Service))
