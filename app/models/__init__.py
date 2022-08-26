from mongoengine import connect
connect(host="mongodb+srv://m0ng0r1y4n:m0ng0r1y4n@cluster0.m3k3p39.mongodb.net/db_1?retryWrites=true&w=majority")
    
from mongoengine import *
from datetime import datetime

class Users(Document):
    userId = StringField(required=True, unique=True)
    userName = StringField(max_length=25, required=True, unique=True)
    userEmail = EmailField(required=True, unique=True)
    userPassword = StringField(required=True)
    userFirstName = StringField(max_length=25)
    userLastName = StringField(max_length=25)
    userPhoneNumber = StringField(max_length=15, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
class Task(Document):
    taskId = StringField(unique=True, required=True)
    taskName = StringField(required=True)
    taskDetail = StringField()
    userId = ReferenceField(Users, reverse_delete_rule=CASCADE)