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
   checkDone = db.Column(db.Integer,default =0)
   notes=  db.Column(db.String(3024))  

   


def __init__(self, name, address, phone, email, cost,timestamp,notes,checkDone):
   self.name = name
   self.address = address
   self.phone = phone
   self.email = email
   self.cost = cost
   self.timestamp = timestamp
   self.notes = notes
   self.checkDone=checkDone 

