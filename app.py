#!/usr/bin/env python3
"""
Host status utility
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse

import utils

APP = Flask(__name__)
api = Api(APP)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(APP)

parser = reqparse.RequestParser()
parser.add_argument('hostname')

class Host(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    ip = db.Column(db.String) 

class Hosts(Resource):
    def get(self):
        return {"hosts": [{'hostname': x.ip, 'up': False} for x in Host.query.all()]}, 200

    def post(self):
        """
        Check a host specified by IP to see if we can resolve it.
        """
        if 'hostname' not in request.get_json():
            return {'error': 'missing hostname'}, 400
        if not utils.is_valid(request.get_json()['hostname']):
            return {'error': 'invalid hostname'}, 400

        new_host = Host(ip=request.get_json()['hostname'])
        db.session.add(new_host)
        db.session.commit()

        return {'up': utils.is_up(request.get_json()['hostname'])}, 200

    def delete(self):
        if 'hostname' not in request.values:
            return {'error': 'missing hostname'}, 400
        existing_host = Host.query.filter_by(ip=request.values['hostname']).first()
        if existing_host is None:
            return {'error': 'no host with ip {}'.format(request.values['hostname'])}, 400
        db.session.delete(existing_host)
        db.session.commit()
        return {}, 200

api.add_resource(Hosts, '/api/hosts')

if __name__ == "__main__":
    db.create_all()
    APP.run(debug=True)
