from importall import *
from datetime import datetime
class contact(db.Model):
   id = db.Column('product_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   message = db.Column(db.String(1024)) 
   phone = db.Column(db.String(100))
   email = db.Column(db.String(100))
   checkDone = db.Column(db.Integer,default =0)
   timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


def __init__(self, name, message, phone, email, checkDone,timestamp):
   self.name = name
   self.message = message
   self.phone = phone
   self.email = email
   self.checkDone=checkDone
   self.timestamp = timestamp






