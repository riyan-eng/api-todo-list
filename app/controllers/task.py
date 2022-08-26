from app import responseHandler, requestStruct, requestMapping, models
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request
from uuid import uuid4
from json_checker import Checker

@jwt_required(fresh=True)
def list():
    try:
        userId = get_jwt_identity()
        collUser = models.Users.objects(userId=userId).first()
        collTask = models.Task.objects(userId=collUser).all()
        dataArray = []
        for d in collTask:
            dataArray.append({
                "taskId": d.taskId,
                "taskName": d.taskName,
                "taskDetail": d.taskDetail
            })
        return responseHandler.ok(dataArray)
    except Exception as e:
        print(e)
        responseJson = {"message": "Error"}
        return responseHandler.badRequest(responseJson)

@jwt_required(fresh=True)
def create():
    bodyJson = request.json
    data = requestMapping.Task(bodyJson)
    try:
        result = Checker(requestStruct.Task(), soft=True).validate(data)
        userId = get_jwt_identity()
        collUser = models.Users.objects(userId=userId).first()
        print(collUser.userName)
        collTask = models.Task(taskId = str(uuid4()), userId=collUser, taskName = result["taskName"], taskDetail = result["taskDetail"])
        collTask.save()
        responseJson = {"message": "Success added task"}
        return responseHandler.ok(result)
    except Exception as e:
        print(e)
        responseJson = {"message": "Error"}
        return responseHandler.badRequest(responseJson)

@jwt_required(fresh=True)        
def read(taskId):
    try:
        userId = get_jwt_identity()
        collUser = models.Users.objects(userId=userId).first()
        collTask = models.Task.objects(userId=collUser, taskId = taskId).first()
        if not collTask:
            responseJson = {"message": "Data doesn't exist"}
            return responseHandler.badRequest(responseJson)
        responseJson = {
            "taskId": collTask.taskId,
            "taskName": collTask.taskName,
            "taskDetail": collTask.taskDetail
        }
        return responseHandler.ok(responseJson)
    except Exception as e:
        print(e)
        responseJson = {"message": "Error"}
        return responseHandler.badRequest(responseJson)

@jwt_required(fresh=True)
def update(taskId):
    bodyJson = request.json
    data = requestMapping.Task(bodyJson)
    try:
        result = Checker(requestStruct.Task(), soft=True).validate(data)
        userId = get_jwt_identity()
        collUser = models.Users.objects(userId=userId).first()
        collTask = models.Task.objects(userId=collUser, taskId = taskId).first()
        if not collTask:
            responseJson = {"message": "Data doesn't exist"}
            return responseHandler.badRequest(responseJson)
        models.Task.objects(taskId = taskId).update(taskName=result["taskName"], taskDetail=result["taskDetail"])
        responseJson = {"message": "Upadate successfully", "taskId" : collTask["taskId"]}
        return responseHandler.ok(responseJson)
    except Exception as e:
        print(e)
        responseJson = {"message": "Error"}
        return responseHandler.badRequest(responseJson)
    
@jwt_required(fresh=True)
def delete(taskId):
    try:
        userId = get_jwt_identity()
        collUser = models.Users.objects(userId=userId).first()
        collTask = models.Task.objects(userId=collUser, taskId = taskId).first()
        if not collTask:
            responseJson = {"message": "Data doesn't exist"}
            return responseHandler.badRequest(responseJson)
        models.Task.objects(taskId = taskId).delete()
        responseJson = {"message": "Delete Successfully", "taskId" : taskId}
        return responseHandler.ok(responseJson)
    except Exception as e:
        print(e)
        responseJson = {"message": "Error"}
        return responseHandler.badRequest(responseJson)
