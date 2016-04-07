#!/usr/bin/env python
import os

#import the main app
from flaskapp import app as application

#define the environment
#if ENV is not defined then default: development
env = os.environ['ENV'] if 'ENV' in os.environ else 'development'

#
# Run the app
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    if env =='production':
      httpd.handle_request()
    else:
      httpd.serve_forever()
