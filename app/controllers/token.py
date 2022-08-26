from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from flask import jsonify
from app import jwt
# from config import jwt_redis_blocklist
from datetime import timedelta

ACCESS_EXPIRES = timedelta(hours=1)

@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    accessToken = create_access_token(identity=identity, fresh=True)
    return jsonify(accessToken=accessToken)

# @jwt.token_in_blocklist_loader
# def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
#     jti = jwt_payload["jti"]
#     token_in_redis = jwt_redis_blocklist.get(jti)
#     return token_in_redis is not None

# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
#     return jsonify(msg="Access token revoked")
