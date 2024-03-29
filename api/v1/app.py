#!/usr/bin/python3
"""
Flask application to serve the application
"""
from flask import Flask
from flask import make_response, jsonify
from api.v1.views import app_views
from models import storage
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_prefixed_env()


jwt = JWTManager(app)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

@app.teardown_appcontext
def close_db(error):
    """ close storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ runs the flask app """
    host = '0.0.0.0'
    port = '5000'

    app.run(host=host, port=port, threaded=True, debug=True)
