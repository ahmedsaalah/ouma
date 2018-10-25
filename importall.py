

from flask import (Flask, render_template, request, redirect,
jsonify, url_for, flash, make_response, session as login_session)

from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import sessionmaker
from datetime import datetime
app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql7262379:Lh3gtVRjgQ@sql7.freemysqlhosting.net/sql7262379'

db = SQLAlchemy(app)
