from re import A
from .endpoints import auth
from .endpoints import user

def initialize_routes(api):
    api.add_resource(auth.AuthApi, '/api/auth')
    api.add_resource(user.UserApi, '/api/user')
 # api.add_resource(auth.AuthApi, '/api/user/<id>')