"""
This file holds the definition of the Mongo Org document
"""

import datetime

from mongoengine import Document, StringField, DateTimeField
from mongoengine import ListField, ReferenceField

from app.models.Service import Service

class Org(Document):
  """
  This class is the ORM for the collection of orgs
  """

  name = StringField(max_length=50, required=True, unique=True)
  date_modified = DateTimeField(default=datetime.datetime.now)
  services = ListField(ReferenceField(Service))
