from routes.home import home_route

def config_all(app):
    config_routes(app)

def config_routes(app):
    app.register_blueprint(home_route)