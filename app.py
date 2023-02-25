from flask import Flask
from routes.contacts import contacts
from config import MYSQL_STRING
app = Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_STRING
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(contacts)
