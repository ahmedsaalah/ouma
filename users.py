from importall import *
class user(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   username = db.Column(db.String(100))

   password = db.Column(db.String(100))


def __init__(self, username,  password):
   self.username = username

   self.password = password


