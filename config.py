from routes.home import home_route
from routes.move import move_route
from main import login_manager

def config_all(app):
    config_routes(app)
    config_login(app)

def config_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(move_route, url_prefix='/move')
    
def config_login(app):
    login_manager.login_view = 'login'
    