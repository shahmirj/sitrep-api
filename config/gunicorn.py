import os

# Set the port from the enviornment
port = 8000
if 'PORT' in os.environ:
    port = os.environ['PORT']

bind = "0.0.0.0:" + str(port)
