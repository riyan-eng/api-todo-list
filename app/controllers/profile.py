from app import responseHandler
from flask_jwt_extended import get_jwt_identity, jwt_required

@jwt_required(fresh=True)
def Profile():
    returnJson = {
        "loginAs": get_jwt_identity()
    }
    return responseHandler.ok(returnJson)