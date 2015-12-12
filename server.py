"""
This is the main server file, It sets all the route
"""

# System setup
import sys, os
sys.path.append("./app");

# Global includes
from flask import Flask, Response, url_for
from flask_restful import Resource, Api

# App includes
from app.controllers.IndexController import IndexController

app = Flask(__name__, static_url_path='/pub')
api = Api(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
      os.path.join(app.root_path, 'static'),
      'favicon.ico',
      mimetype='image/vnd.microsoft.icon'
    )

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
