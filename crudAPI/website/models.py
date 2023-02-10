
from website import db,app
from flask_user import UserManager,UserMixin,SQLAlchemyAdapter

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200),unique =  True)
    email = db.Column(db.String(200),unique = True)
    
    def __repr__(self) -> str:
        return self.email
    
class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key  = True)
    username = db.Column(db.String(30),nullable = False, unique = True)
    email = db.Column(db.String(30),nullable = False, unique = True)
    password = db.Column(db.String(300),nullable = False,server_default= '')
    is_staff = db.Column(db.Boolean(),server_default='1')
    is_active = db.Column(db.Boolean(),server_default='0')
    is_admin = db.Column(db.Boolean(),server_default='0')
    is_superuser = db.Column(db.Boolean(),server_default='0')
    
    def __repr__(self) -> str:
        return self.username
    
db_adapter = SQLAlchemyAdapter(db,Users)
user_manager = UserManager(db_adapter,app)