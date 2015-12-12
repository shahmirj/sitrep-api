#!/usr/bin/env python

from app.models.Mongo import Mongo
from pymongo.database import CollectionInvalid

"""
This function will setup the collections if they don't exist
"""
def main():
  db = Mongo().get_client().get_default_database()
  createCollections(db)
  createIndexes(db)

"""
Given a database set create collections
"""
def createCollections(db):
  for collection in [ 'users', 'orgs', 'services' ]:
    try:
      db.create_collection(collection)
    except CollectionInvalid as e:
      print "'" + collection + "' already exists! Skipped."

"""
Given a database set the default indexes required
"""
def createIndexes(db):
  pass

if __name__ == '__main__':
    main()
