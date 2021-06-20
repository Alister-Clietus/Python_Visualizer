from . import db
from flask_login import UserMixin

class User(db.model,UserMixin):
    id=db.column(db.Integer,primary_key=True)
    First_Name=id.column(db.String(20),primary_key=True)
    Second_Name=id.column(db.String(20),primary_key=True)
    User_Name=id.column(db.String(10),unique=True)
    Email=id.column(db.String(10),unique=True)
    Password=id.column(db.String(200))
