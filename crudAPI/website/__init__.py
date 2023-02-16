from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app =  Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'd4c516c7e3b267a33db6a317ffab126b1bc85ccc2d4d2b2fd5e169c34877'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@localhost/myflaskproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = app.debug
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_DEFAULT_SENDER'] = None
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_SUPPRESS_SEND'] = app.testing
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.config['USER_SEND_PASSWORD_CHANGED_EMAIL']=False
app.config['USER_SEND_REGISTERED_EMAIL']=False
app.config['USER_SEND_USERNAME_CHANGED_EMAIL']=False 
app.config['USER_ENABLE_EMAIL']=True
db = SQLAlchemy(app)
ma = Marshmallow(app)
from website import routes
