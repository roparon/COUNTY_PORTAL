from flask import Blueprint
from flask_security import login_required, current_user
from app.models.user import User


auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/profile')
def profile():
    "This is the current user information"
    # return {
    #     "id": current_user.id,
    #     "email": current_user.email,
    #     "active": current_user.active
    # }
    return f"{current_user.email} is logged in"
    



@auth_bp.route('/users')
@login_required
def users():
    all_users = User.querry.all()
    for user in all_users:
        return f"{user.email} is logged in"