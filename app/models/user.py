from app.extensions import db
from flask_security import UserMixin, RoleMixin
import uuid

# This is the association table for many-to-many relationship between users and roles 
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)

class User(db.Model):
    __tablename__ = 'users'
    # This is basic identity fielsds that comes with Flask-Security

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    #flask-security required fields for tokens, sessions, password management
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))



class Role(db.Model):
    __tablename__ = 'roles'
    # This is basic identity fielsds that comes with Flask-Security
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))
    # This is the many-to-many relationship with users
    users = db.relationship('User', secondary=roles_users, backref=db.backref('roles', lazy='dynamic'))