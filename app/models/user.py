from app.extensions import db
from flask_security import UserMixin, RoleMixin

# many to many relationship table btween users and roles
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



class Role(db.Model):
    pass