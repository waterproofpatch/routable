#!/usr/bin/env python3
"""
Host status utility
"""

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
    res = {}
    if 'hosts' not in request.args:
        return jsonify({'error': 'invalid hostname'}), 400
    hosts_to_check = request.args['hosts']
    for host in hosts_to_check:
        if not utils.is_valid(request.args['hostname']):
            return jsonify({'error': 'invalid hostname'}), 400
        res['hostname']=utils.is_up(hostname=host)
    return jsonify(res)

@APP.route('/api/check_host_at_index')
def check_host_at_index():
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
