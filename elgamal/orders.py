from importall import *
class orders(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   time = db.Column(db.String(100))  
   quantity1 = db.Column(db.String(200))
   quantity2 = db.Column(db.String(10))
   price = db.Column(db.String(10))
   company_id = db.Column( db.Integer)
   taxes = db.Column( db.Integer)
   discount = db.Column( db.Integer)
   paymentDay = db.Column(db.String(200))

def __init__(self, name, time, company_id,quantity2, quantity1, price ,paymentDay):
   self.price = price
   self.taxes = taxes
   self.discount = discount
   self.time = time
   self.quantity1 = quantity1
   self.quantity2 = quantity2
   self.company_id = company_id
   self.paymentDay = paymentDay
