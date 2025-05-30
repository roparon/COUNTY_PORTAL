from flask import Blueprint
from flask_security import login_required, current_user, roles_required



main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
@login_required
def index():
    return f"Welcome to County Portal! {current_user.email} "


@main_bp.route('/about')
def about():
    return "This is the County Portal application. It provides various services and information related to county operations."


@main_bp.route('/dashboard')
@roles_required('super_admin')
def dashboard():
    return "This is the dashboard where is accesible for admin only!"

