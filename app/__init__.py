from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config')
migrate = Migrate(app)
manager = Manager(app)

from app.controllers import default, functions
