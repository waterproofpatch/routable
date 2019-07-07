#!/usr/bin/env python3
"""
Host status utility
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import utils

APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(APP)

class Host(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    ip = db.Column(db.String) 

@APP.route('/api/check_host')
def check_host():
    """
    Check a host specified by IP to see if we can resolve it.
    """
    if 'hostname' not in request.args:
        return jsonify({'error': 'missing hostname'}), 400
    if not utils.is_valid(request.args['hostname']):
        return jsonify({'error': 'invalid hostname'}), 400

    new_host = Host(ip=request.args['hostname'])
    db.session.add(new_host)
    db.session.commit()

    return jsonify({'up': utils.is_up(request.args['hostname'])}), 200

@APP.route('/api/hosts')
def hosts():
    """
    Get the list of hosts from the database
    """
    return jsonify({"hosts": [{'hostname': x.ip, 'up': False} for x in Host.query.all()]})

if __name__ == "__main__":
    db.create_all()
    APP.run(debug=True)
