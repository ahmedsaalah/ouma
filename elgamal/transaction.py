

from importall import *

class transaction(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   details = db.Column(db.String(200))  
   paid = db.Column(db.Integer)
   left = db.Column(db.Integer)
   time = db.Column(db.DateTime, default=db.func.current_timestamp())
   name = db.Column(db.String(200))


def __init__(self, details, paid,left,name):
   self.details = details
   self.paid = paid
   self.left = left
   self.name = name


