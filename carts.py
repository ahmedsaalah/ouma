from importall import *
from datetime import datetime
class cart(db.Model):
   id = db.Column('cart_id', db.Integer, primary_key = True)
   product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'),nullable=False)
   order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'),nullable=False)
   occur = db.Column(db.Integer)
   notes=  db.Column(db.String(3024))  



def __init__(self, product_id, order_id,occur,notes):
   self.product_id = product_id
   self.order_id = order_id
   self.occur = occur
   self.notes = notes



