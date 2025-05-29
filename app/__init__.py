from flask import Flask
from app.extensions import db
from app.extensions import db, migrate
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)



    with app.app_context():
        db.create_all()
    return app


