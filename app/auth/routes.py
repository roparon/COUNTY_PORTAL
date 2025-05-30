from flask import Blueprint
from flask_security import login_required, current_user


auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/profile')
def profile():
    "This is the current user information"
    return {
        "id": current_user.id,
        "email": current_user.email,
        "active": current_user.active
    }
    