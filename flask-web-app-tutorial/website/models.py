from . import db                #import from current package 
from flask_login import UserMixin               #custom class somethings for flask login
from sqlalchemy.sql import func             #sqlalchemy gets current date & time
from sqlalchemy import Column, Integer, ForeignKey


class Note(db.Model):
    # __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)                
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db. Integer, db.ForeignKey('user.id'))
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key referencing the User table


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    is_active = db.Column(db.Boolean, default=True)
    notes = db.relationship('Note')                 