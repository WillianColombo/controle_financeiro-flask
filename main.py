from flask import Flask
from config import config_all
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
login_manager = LoginManager(app)    
bcrypt = Bcrypt(app)

config_all(app)

app.run(debug=True)