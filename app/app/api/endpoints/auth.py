from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from ..models import User
import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

class AuthApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        
        access_token = create_access_token(identity=str(user.id), expires_delta=datetime.timedelta(seconds=5))
        refresh_token = create_refresh_token(identity=str(user.id), expires_delta=datetime.timedelta(days=30))
        return {'token': access_token, 'refresh_token': refresh_token}, 200

class RefreshAuthApi(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {'access_token': access_token}


