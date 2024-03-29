from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security_new import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
# if DATABASE_URL on heroku is not accessible then sqlite db will work. so on our local system will work with sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key='secret'
api = Api(app)

jwt = JWT(app,authenticate,identity) #JWT creates an endpoint /auth


api.add_resource(Item, '/item/<string:name>')

api.add_resource(ItemList, '/items')

api.add_resource(UserRegister,'/register')

api.add_resource(Store, '/store/<string:name>')

api.add_resource(StoreList, '/stores')

if __name__ == "__main__":

    from db import db
    db.init_app(app)
    # it only runs if the file is run directly, it won't run on importing the file to other file
    app.run(port=5000, debug = True)