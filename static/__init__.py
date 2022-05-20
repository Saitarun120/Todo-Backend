from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

from static.logger_config import custom_logger

db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger('gunicorn.error')
logger = custom_logger(logger)
cors = CORS()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://geyyoblvruhcju:074a07990437a7f82f7097f3448d854417bb5a59013f1737005dbdb6d9b28e51@ec2-34-236-94-53.compute-1.amazonaws.com:5432/d5oj22p22j7em'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from static.todoApp.model.todo_list_model import Todo
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resource={r"/api/*": {"origins": "*"}})

    from static.todoApp import todo_list

    app.register_blueprint(todo_list, url_prefix='/api/v1')

    return app
