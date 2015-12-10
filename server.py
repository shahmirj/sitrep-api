##
# This is the main server file, It sets all the routes
#
#

from flask import Flask
import os

app = Flask(__name__)

# Routing
@app.route("/")
def hello():
    return "Hello World!"

# Set the port from the enviornment
PORT = 80
if 'PORT' in os.environ:
    PORT = os.environ['PORT']

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=PORT
    )
