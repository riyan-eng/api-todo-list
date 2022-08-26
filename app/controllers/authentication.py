from flask import request
from app import responseHandler, requestStruct, requestMapping, models
from json_checker import Checker
from hashlib import sha256
from uuid import uuid4
from flask_jwt_extended import create_access_token, create_refresh_token

def register():
    try:
        bodyJson = request.json
        data = requestMapping.Register(bodyJson)
        try:
            result = Checker(requestStruct.Register(), soft=True).validate(data)
            if result["userPassword1"] != result["userPassword2"]:
                responseJson = {"message": "Password didn't match"}
                return responseHandler.badRequest(responseJson)

            query = models.Users.objects(userName=result["userName"])
            if query:
                responseJson = {"message": "Username has been used."}
                return responseHandler.badRequest(responseJson)
            
            query = models.Users.objects(userEmail=result["userEmail"])
            if query:
                responseJson = {"message": "Email has been used."}
                return responseHandler.badRequest(responseJson)
            
            query = models.Users.objects(userPhoneNumber=result["userPhoneNumber"])
            if query:
                responseJson = {"message": "Phone number has been used."}
                return responseHandler.badRequest(responseJson)
            
            password = result["userPassword1"] + "secret"
            userPassword = sha256(password.encode("utf-8")).hexdigest()
            doc = models.Users(userId = str(uuid4()), userName = result["userName"], userEmail = result["userEmail"], userPassword = userPassword, userFirstName = result["userFirstName"], userLastName = result["userLastName"], userPhoneNumber = result["userPhoneNumber"])
            doc.save()
            responseJson = {
                "data": {
                    "userName": result["userName"],
                    "userEmail": result["userEmail"]
                },
                "message": "User has been created."
            }
            return responseHandler.ok(responseJson)
        except Exception as e:
            print(e)
            responseJson = {"message": "Input invalid."}
            return responseHandler.badRequest(responseJson)
    except Exception as e:
        print(e)
        responseJson = {"message": "System under maintenance"}
        return responseHandler.badRequest(responseJson)

def login():
    try:
        bodyJson = request.json
        data = requestMapping.Login(bodyJson)
        try:
            result = Checker(requestStruct.Login(), soft=True).validate(data)
            password = result["userPassword"] + "secret"
            userPassword = sha256(password.encode("utf-8")).hexdigest()
            query = models.Users.objects(userName=result["userName"], userPassword = userPassword).first()
            if not query:
                responseJson = {"message": "Username or password invalid."}
                return responseHandler.badRequest(responseJson)
            
            responseJson = {
                "userId": query.userId,
                "userName": query.userName,
                "userEmail": query.userEmail,
                "userFirstName": query.userFirstName,
                "userLastName": query.userLastName,
                "userPhoneNumber": query.userPhoneNumber,
                "accessToken": create_access_token(identity=query.userId, fresh=True),
                "refreshToken": create_refresh_token(identity=query.userId)
            }
            # responseJson = {
            #     "id": query.userId,
            #     "username": query.userName,
            #     "firstName": query.userFirstName,
            #     "lastName": query.userLastName,
            #     "token": create_access_token(identity=query.userName, fresh=True)
            # }
            return responseHandler.ok(responseJson)
        except Exception as e:
            print(e)
            responseJson = {"message": "Input invalid."}
            return responseHandler.badRequest(responseJson)
    except Exception as e:
        print(e)
        responseJson = {"message": "System under maintenance"}
        return responseHandler.badRequest(responseJson)