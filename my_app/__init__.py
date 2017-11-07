'''
This is the server init file ... when a user hits the endpoint this will respond.
'''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test3.db'
db = SQLAlchemy(application)
api = Api(application)
 
from my_app.user.views import catalog
application.register_blueprint(catalog)


 
db.create_all()

