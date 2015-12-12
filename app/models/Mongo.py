"""
This file holds the definition of our Mongo class

@author Shahmir Javaid
"""

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
      Mongo.client = MongoClient();

    return Mongo.client

  """
  Get the instance of the database from the client
  """
  @staticmethod
  def get_database():
    return Mongo.client.mydb
