from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from ..models import User
import datetime

class AuthApi(Resource):
    def get(self):
        return Response({
            'accessToken': 'Hello World', 
            'refreshToken': 'World Hello'
            }, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200

    def delete(self, id):
        return '', 200
    
    # def get(self, id):
    #     return {'accessToken': 'get byId', 'refreshToken': 'get by id'}, 200

