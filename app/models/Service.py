from mongoengine import *
import datetime

class Service(Document):
  """
  This class is the ORM for the collection of services
  """

  name = StringField(max_length=50, required=True)
  description = StringField(max_length=300)
  date_modified = DateTimeField(default=datetime.datetime.now)
