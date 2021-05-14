from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
#
from .api.routes import initialize_routes
from .api.db import initialize_db


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    # 'db': 'mydb',
    # 'host': 'localhost',
    # 'port': 27017,
    # 'username':'root',
    # 'password':'example'
    'host': 'mongodb://root:example@localhost:27017/mydb?authSource=admin'
}

app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
