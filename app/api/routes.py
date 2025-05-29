from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')


@api_bp.route('/users', methods=['GET'])
def users_list():
    return [{"name": "John Doe", "email": "john.doe@example.com"}, 
            {"name": "Jane Smith", "email": "jane.smith@example.com"}, 
            {"name": "Alice Johnson", "email": "alice.johnson@example.com"}]

