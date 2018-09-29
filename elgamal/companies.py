from importall import *
class company(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   address = db.Column(db.String(100))  
   telephone = db.Column(db.String(200))
   price1 = db.Column(db.String(10))
   price2 = db.Column(db.String(10))

def __init__(self, name, address, telephone, price1, price2):
   self.name = name
   self.address = address
   self.telephone = telephone
   self.price1 = price1
   self.price2 = price2
