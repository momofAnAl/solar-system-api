from flask import Flask
from app.db import db, migrate
from app.routes.planets_routes import planet_bp
import os


def create_app(config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    if config:
        app.config.update(config)
    

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(planet_bp)

    return app
