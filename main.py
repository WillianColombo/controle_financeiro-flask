from flask import Flask
from config import config_all
from extensions import login_manager, bcrypt

app = Flask(__name__)

login_manager.init_app(app)
bcrypt.init_app(app)

config_all(app)

app.run(debug=True)