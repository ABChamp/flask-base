from flask import Response, request
from flask_restful import Resource
from ..models import User
from flask_jwt_extended import jwt_required

class UserApi(Resource):
    @jwt_required()
    def get(self):
        user = User.objects().to_json()
        return Response(user, mimetype="application/json", status=200)
        # return Response({
        #     'accessToken': 'Hello World', 
        #     'refreshToken': 'World Hello'
        #     }, mimetype="application/json", status=200)

    # create user
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        ## save
        return {'id': str(id)}, 200
    
    def delete(self, id):
        return '', 200
    
    # def get(self, id):
    #     return {'accessToken': 'get byId', 'refreshToken': 'get by id'}, 200

