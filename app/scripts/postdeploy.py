#!/usr/bin/env python

from app.models.Mongo import Mongo
from pymongo.database import CollectionInvalid

def main():
  db = Mongo().get_client().get_default_database()
  for collection in [ 'users', 'orgs', 'services' ]:
    try:
      db.create_collection(collection)
    except CollectionInvalid as e:
      print "'" + collection + "' already exists! Skipped."

if __name__ == '__main__':
    main()
