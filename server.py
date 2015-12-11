##
# This is the main server file, It sets all the routes
#
#

from flask import Flask

app = Flask(__name__)

# Routing
@app.route("/")
def hello():
    return "Hello dev world!"
