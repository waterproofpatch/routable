#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import jsonify

import utils

APP = Flask(__name__)

@APP.route('/api/update')
def index():
    """
    Index page
    """
    return 'Hello World'

@APP.route('/api/check_host')
def check_host():
    """
    Index page
    """
    if 'hostname' not in request.args:
        return jsonify({'error': 'missing hostname'}), 400
    if not utils.is_valid(request.args['hostname']):
        return jsonify({'error': 'invalid hostname'}), 400
    return jsonify({'up': utils.is_up(request.args['hostname'])}), 200

    return {}

if __name__ == "__main__":
    APP.run(debug=True)
