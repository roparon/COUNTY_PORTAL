from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    return "Welcome to County Portal!"


@main_bp.route('/about')
def about():
    return "This is the County Portal application. It provides various services and information related to county operations."