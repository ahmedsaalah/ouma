from importall import *
from datetime import datetime
class order(db.Model):
   id = db.Column('order_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   address = db.Column(db.String(1024)) 
   phone = db.Column(db.String(100))
   email = db.Column(db.String(100))
   cost = db.Column( db.Integer)
   timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
   


def __init__(self, name, address, phone, email, cost,timestamp):
   self.name = name
   self.address = address
   self.phone = phone
   self.email = email
   self.cost = cost
   self.timestamp = timestamp


