from __future__ import print_function # In python 2.7
import sys
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from my_app import db, application, api
from my_app.user.models import User, Fruit
from my_app.auth import requires_auth 
 
catalog = Blueprint('catalog', __name__)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('price', type=float)
parser.add_argument('password', type=str)
parser.add_argument('fruit', type=str)


@catalog.route('/')
@catalog.route('/home')
@requires_auth
def home():
    return "Welcome to the Catalog Home."
 
 
class UserApi(Resource):
 
    def get(self, id=None, page=1):
        if not id:
            users = User.query.paginate(page, 10).items
        else:
            users = [User.query.get(id)]
        res = {}
        for user in users:
            res[user.id] = {
                'name': user.name,
                'price': str(user.price),
            }
        return json.dumps(res)
 
    def post(self):
        args = parser.parse_args()
        name = args['name']
        price = args['price']
        password = args['password']
        user = User(name, price, password)
        db.session.add(user)
        db.session.commit()
        res = {}
        res[user.id] = {
            'name': user.name,
            'password': user.password,
        }
        return json.dumps(res)
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        args = parser.parse_args()
        fruit = args['fruit']

        users = [User.query.get(id)]
        res = {}
        for user in users:
            user.fruits.append(Fruit(fruit))
            res[user.id] = {
                'name': user.name,
                'first_fruit': user.fruits[0].name,
            }
        return json.dumps(res)

    def delete(self, id):
        # Delete the record for the provided id.
        return
 
api.add_resource(
   UserApi,
   '/api/user',
   '/api/user/<int:id>',
   '/api/user/<int:id>/<int:page>'
)
