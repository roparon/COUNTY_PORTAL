from flask import Blueprint, redirect, url_for, render_template, requests
from flask_security import login_required, current_user, roles_required
from app.models.user import User, Role
from app.models.county import County, Department
from app.utils.constants import UserRoles


auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/profile')
@login_required
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
    

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_bp.index'))