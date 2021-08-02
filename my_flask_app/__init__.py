from flask import Flask
from flask_mysqldb import MySQL

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dummy"
    app.config['MYSQL_HOST'] = 'flaskdb.ckw0txmoaupk.us-west-2.rds.amazonaws.com'
    app.config['MYSQL_USER'] = 'admin'
    app.config['MYSQL_PASSWORD'] = 'admin1234'
    app.config['MYSQL_DB'] = 'flaskapp'

    mysql = MySQL(app)

    from .views import view
    from .auth import auth

    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
