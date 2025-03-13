import time
import pymysql
from flask import Flask
from models import *
from sqlalchemy.exc import OperationalError


def create_app():
    pymysql.install_as_MySQLdb()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@mysql:3306/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    while True:
        try:
            with app.app_context():
                db.create_all()
            print("Successfully connected to MySQL and database tables created!")
            break
        except OperationalError as e:
            print(f"Error connecting to MySQL: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

    from routes import register_routes
    register_routes(app, db)

    return app
