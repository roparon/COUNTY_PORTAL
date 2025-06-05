from flask import Blueprint, render_template, redirect, url_for
from flask_security import login_required, current_user
from app.utils.constants import UserRoles



main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')                                                           
def index():                                                                  
    """Home page - redirect based on authentication status"""                 
    if current_user.is_authenticated:                                         
        return redirect(url_for('main_bp.dashboard'))                         
    return render_template('main/index.html')


@main_bp.route('/about')
def about():
    return "This is the County Portal application. It provides various services and information related to county operations."


@main_bp.route('/dashboard')                                                  
@login_required                                                               
def dashboard():                                                              
    """Role-based dashboard routing"""                                        
    if current_user.has_role(UserRoles.SUPER_ADMIN):                          
        return redirect(url_for('main_bp.admin_dashboard'))                   
    elif current_user.has_role(UserRoles.STAFF):                              
        return redirect(url_for('main_bp.staff_dashboard'))                   
    elif current_user.has_role(UserRoles.CITIZEN):                            
        return redirect(url_for('main_bp.citizen_dashboard'))                 
    else:                                                                     
        return redirect(url_for('main_bp.guest_dashboard'))
