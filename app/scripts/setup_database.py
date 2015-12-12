#!/usr/bin/env python
"""
This file holds functions used to run the setup for a database

Use the main function to run the setup procedure. Non main function
individual functions are used to make things nice
"""

from pymongo.database import CollectionInvalid
from app.models.Mongo import Mongo


def main():
  """
  This function will setup the collections if they don't exist
  """
  database = Mongo().get_db()
  create_collections(database)


def create_collections(database):
  """
  Given a database set create collections
  """
  for collection in ['users', 'orgs', 'services']:
    try:
      database.create_collection(collection)
    except CollectionInvalid:
      print "'" + collection + "' already exists! Skipped."

if __name__ == '__main__':
  main()
