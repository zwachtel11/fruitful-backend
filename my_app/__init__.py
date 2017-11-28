'''
This is the server init file ... when a user hits the endpoint this will respond.
'''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test6.db'
db = SQLAlchemy(app)
api = Api(app)
 
from my_app.user.views import catalog
app.register_blueprint(catalog)


 
db.create_all()

