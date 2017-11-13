from my_app import db
import datetime
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    price = db.Column(db.Float(asdecimal=True))
    fruits = db.relationship('Fruit', backref='user', uselist=True, lazy=True)
 
    def __init__(self, name, password):
        self.name = name
        self.password = password
 
    def __repr__(self):
        return '<User %d>' % self.id

    def get_count(self):
        return len(self.fruits)

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id
    def __repr__(self):
        return '<Fruit %d>' % self.id

    


    