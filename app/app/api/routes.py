from re import A
from .endpoints import auth
from .endpoints import user

def initialize_routes(api):
    api.add_resource(auth.AuthApi, '/api/auth')
    api.add_resource(auth.RefreshAuthApi, '/api/auth/refresh')
    api.add_resource(user.UserApi, '/api/user')