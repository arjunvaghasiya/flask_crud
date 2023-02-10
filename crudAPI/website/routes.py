from website import api,db,app
from flask_restful import Resource,request
from .models import Employee
from .serializer import EmployeeGetSerializer, EmployeeSerializer,EmployeeGetOneSerializer
from flask import jsonify,request,Flask
from flask_user import login_required

class CreateEmployee(Resource):
    
    def post(self):
        data = request.get_json()
        
        user = Employee(
            username= data.get('username'),
            email = data.get('email')  
        )
        db.session.add(user)
        db.session.commit()
        serializer = EmployeeGetSerializer()
        data = serializer.dump(user)
        context = {}
        context = {"id":data['id'],
            "username":data['username'],
            "email":data['email']  
        }
        return jsonify(data),201


class EmployeeList(Resource):

    def get(self):
        user = Employee.query.all()
        serializer = EmployeeSerializer(user)
        return serializer, 200


class EmployeeUpdate(Resource):
    
       def put(self,id):
        try:  
            # import pdb;pdb.set_trace()      
            user = Employee.query.get(int(id))
            user.email = request.json['email']
            db.session.add(user)
            db.session.commit()
            return 201
        except Exception as e:
            return jsonify({'Error':'somthing is wrong'})
        
class EmployeeGEt(Resource):
        
        def get(self,id):
            try:  
                # import pdb;pdb.set_trace()  
                user = Employee.query.get(int(id))
                serializer = EmployeeGetOneSerializer()
                data = serializer.dump(user)
                return jsonify(data["username"])
            
            except Exception as e:
                return jsonify({'Error':'somthing is wrong'})
            
# @app.route('/login')

# def login_fun():
#     return '<h1> You Loged in now</h1>'
class UserLogin(Resource):
        @login_required
        def get(self):
            import pdb;pdb.set_trace()
            print(self[0].username)
            return 'Logged in'                  

api.add_resource(CreateEmployee,"/")
api.add_resource(EmployeeList,"/emplist")
api.add_resource(EmployeeUpdate,"/emp/<int:id>")
api.add_resource(EmployeeGEt,"/emp/<int:id>")
api.add_resource(UserLogin,"/login")