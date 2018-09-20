from importall import *
class product(db.Model):
   id = db.Column('product_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   price = db.Column(db.Integer)  
   oldPrice = db.Column(db.Integer)
   picture = db.Column(db.String(256))
   category = db.Column(db.Integer)
   rate = db.Column(db.Integer)


def __init__(self, name, price, oldPrice, picture, category, rate):
   self.name = name
   self.price = price
   self.oldPrice = oldPrice
   self.picture = picture
   self.category = category
   self.rate = rate





