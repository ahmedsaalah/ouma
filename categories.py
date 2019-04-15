from importall import *
class category(db.Model):
   id = db.Column('category_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))



def __init__(self, name):
   self.name = name






