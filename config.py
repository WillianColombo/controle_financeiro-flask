from routes.home import home_route
from routes.move import move_route
from routes.user import user_route
from dotenv import load_dotenv
from database.database import db
from database.models.user import User
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
    db.create_tables([User])

def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(move_route, url_prefix='/move')
    app.register_blueprint(user_route, url_prefix='/user')
    
def config_login(app):
    from extensions import login_manager
    login_manager.login_view = 'login'