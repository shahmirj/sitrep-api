"""
This file holds the definition of our Mongo class

@author Shahmir Javaid
"""

import os
from pymongo import MongoClient

class Mongo(object):
  """
  This is a class helper that stores the mongo connection
  and loads it up. It is easy to call this function to get
  the connection
  """

  client = None

  def __init__(self):
    """
    The default construction
    """
    pass


  @staticmethod
  def get_client():
    """
    Get the instance of the mongo client
    """
    if Mongo.client is None:
      connection_string = os.environ.get(
          'MONGOLAB_URI',
          'mongodb://127.0.0.1:27017/sitrep_testing'
      )
      Mongo.client = MongoClient(connection_string)

    return Mongo.client

  @staticmethod
  def get_db():
    """
    A helpful wrapper for get_default_database
    """
    return Mongo.get_client().get_default_database()
