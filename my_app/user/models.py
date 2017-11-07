from my_app import db
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    price = db.Column(db.Float(asdecimal=True))
    fruits = db.relationship('Fruit', backref='user', lazy=True)
 
    def __init__(self, name, price, password):
        self.name = name
        self.price = price
        self.password = password
 
    def __repr__(self):
        return '<User %d>' % self.id

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Fruit %d>' % self.id

    


    