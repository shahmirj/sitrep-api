"""
This is the main server file, It sets all the route
"""

# System setup
import sys, os
sys.path.append("./app");

# Global includes
from flask import Flask, Response
from flask_restful import Resource, Api

# App includes
from controllers.IndexController import IndexController

app = Flask(__name__)
api = Api(app)

# Add the resources for routing
api.add_resource(IndexController, "/")

enviornment = os.environ.get('APPLICATION_ENV','production')
print "Enviornment set to " + enviornment + "."

# Set to debug if enviornment is set to testing or development
if enviornment == "testing" or enviornment == "development":
  debug=True
else:
  debug=False


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=debug)
