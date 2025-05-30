from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from app.extensions import db
from app.extensions import db, migrate
from app.models.user import User, Role
from config import Config
from app.extensions import mail, security

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)


    # Register the blueprints
    # Blueprints import
    from app.main.views import main_bp
    from app.api.routes import api_bp
    from app.auth.routes import auth_bp

    # Register the API blueprint
    # Register the blueprint
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    # Import models abd initialize flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    from flask_security import hash_password
    import uuid



    with app.app_context():
        db.create_all()

        roles_data = [
            {'name': 'super_admin', 'description': 'Administrator role with full access'},
            {'name': 'staff', 'description': 'Staff role with limited access'},
            {'name': 'citizen', 'description': 'Citizen role with basic access'},
            {'name': 'guest', 'description': 'Guest role with minimal access'}
        ]

        for role_data in roles_data:
            role = Role.query.filter_by(name=role_data['name']).first()
            if not role:
                role = Role(**role_data)
                db.session.add(role)
            
            admin_role = Role.query.filter_by(name='super_admin').first()
            admin_user = User.query.filter_by(email='aaronrop40@gmail.com').first()


            if not admin_user:
                admin_user = User(
                    email='aaronrop40@gmail.com',
                    password=hash_password('12345678',),
                    active=True,
                    roles=[admin_role],
                    fs_uniquifier= str(uuid.uuid4())
                )
                admin_role.users.append(admin_role)
                db.session.add(admin_user)
            db.session.commit()
            print("Database initialized with admin user and roles.")



    return app


