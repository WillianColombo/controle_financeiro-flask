from routes.home import home_route
from routes.move import move_route
from routes.user import user_route
from routes.control import control_route
from routes.nature import nature_route
from dotenv import load_dotenv
from database.database import db
from database.models.user import User
from database.models.contact import Contact
from database.models.control import Control
from database.models.estimate import Estimate
from database.models.move import Move
from database.models.type_move import TypeMove
from database.models.nature import Nature
import os

def config_all(app):
    config_routes(app)
    config_env(app)
    config_login(app)
    configure_db()
    
def config_env(app):
    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
def configure_db():
    db.connect()
    db.create_tables([User, Contact, Control, TypeMove, Nature, Estimate, Move])

def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(move_route, url_prefix='/move')
    app.register_blueprint(user_route, url_prefix='/user')
    app.register_blueprint(control_route, url_prefix='/control')
    app.register_blueprint(nature_route, url_prefix='/nature')
    
def config_login(app):
    from extensions import login_manager
    login_manager.login_view = 'login'