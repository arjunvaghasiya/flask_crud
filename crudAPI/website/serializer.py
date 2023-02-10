from .models import Employee


def EmployeeSerializer(employees : Employee):
    serializer = []
    for emp in employees:
        emp_dict = {
            "username" : emp.username,
            "email" : emp.email
        }
        serializer.append(emp_dict)
    return serializer
        


from marshmallow import Schema,fields
class EmployeeGetSerializer(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    
class EmployeeGetOneSerializer(Schema):
    id = fields.Integer()
    username = fields.String()
