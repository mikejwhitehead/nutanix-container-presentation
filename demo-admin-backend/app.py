from os import getenv

from flask import Flask, render_template
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_restful import Api

import settings

from exceptions.demoadmin_validation_exception import DemoAdminValidationException

class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        # Tell browsers to only cache the API docs file for 5 seconds (as opposed
        # to the default 12 hours) since it changes frequently
        if name == 'openapi.yaml':
            return 5
        super(self, MyFlask).get_send_file_max_age(name)


flask_app = MyFlask('demo-admin-backend', static_url_path="/api_static")
logger = flask_app.logger
logger.setLevel('DEBUG')

CORS(flask_app, resources={r"/api/*": {"origins": "*"}})
DB_NAME = settings.DB_NAME
DB_HOST = settings.DB_HOST
DB_PORT = settings.DB_PORT
MONGO_URI = f"mongodb://{DB_HOST}:{DB_PORT}/{DB_NAME}"

# for Flask-PyMongo
flask_app.config["MONGO_URI"] = MONGO_URI
flask_app.config['MONGODB_CONNECT'] = False

# for Flask-MongoEngine
flask_app.config['MONGODB_SETTINGS'] = {
    'host': MONGO_URI,
    'connect': False
}

class MyApi(Api):
    def handle_error(self, e):
        # Format Demo Admin App errors
        if isinstance(e, DemoAdminValidationException):
            return self.make_response({'errors': [{'message': error} for error in e.errors]}, 400)
        return super(MyApi, self).handle_error(e)


flask_api = MyApi(flask_app)
mongo = PyMongo(flask_app)
mongoengine = MongoEngine(flask_app)


@flask_app.route('/api-docs')
def api_docs_view():
    return render_template('openapi.html')


from resources.contacts import Contact, Contacts
flask_api.add_resource(Contacts, '/api/contacts')
flask_api.add_resource(Contact, '/api/contacts/<string:id_str>')

