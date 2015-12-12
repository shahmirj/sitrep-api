"""
This file holds the definition of our Mongo class

@author Shahmir Javaid
"""

import sys
import os

from pymongo import MongoClient

"""
This is a class helper that stores the mongo connection
and loads it up. It is easy to call this function to get
the connection
"""
class Mongo:

  client = None

  """
  Get the instance of the mongo client
  """
  @staticmethod
  def get_client():
    if Mongo.client == None:
      connection_string = os.environ.get(
        'MONGOLAB_URI',
        'mongodb://127.0.0.1:27017/sitrep'
      );
      Mongo.client = MongoClient(connection_string);

    return Mongo.client
