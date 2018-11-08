from importall import *
from datetime import datetime
class aboutdb(db.Model):
   id = db.Column('about_id', db.Integer, primary_key = True)

   message = db.Column(db.String(3024)) 
   img = db.Column(db.String(1024)) 



def __init__(self,  message,img):

   self.message = message
   self.img =img







