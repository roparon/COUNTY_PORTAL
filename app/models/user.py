from app.extensions import db



class User(db.Model):
    __tablename__ = 'users'
    # This is basic identity fielsds that comes with Flask-Security

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)