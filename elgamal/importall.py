from flask import Flask


from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import sessionmaker
from datetime import datetime
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/camel'

db = SQLAlchemy(app)
