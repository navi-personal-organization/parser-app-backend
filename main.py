import time
import logging
from flask import Flask
from flask_cors import CORS
from flask_script import Manager
from app.modules.cases.api import cases
from app.modules.cases.service import CasesService as service

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.register_blueprint(cases)

CORS(app)
manager = Manager(app)


@manager.command
def runserver():
    service.parse_csv()
    app.run()


if __name__ == "__main__":
    manager.run()