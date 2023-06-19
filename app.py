from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db

from resources.user.user  import blp as UserBlueprint

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Art Corner REST API"
    app.config["API_VERSION"] = "v1"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "mysql+pymysql://root:root@localhost:3306/art-corner"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    # api = Api(app)

    app.config["JWT_SECRET_KEY"] = "mithun"
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(UserBlueprint)

    return app