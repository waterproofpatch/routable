#!/usr/bin/env python3

from flask import Flask

APP = Flask(__name__)

@APP.route('/api/update')
def index():
    """
    Index page
    """
    return 'Hello World'

if __name__ == "__main__":
    APP.run(debug=True)
