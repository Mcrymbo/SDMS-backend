#!/usr/bin/python3
"""
Flask application to serve the application
"""
from flask import Flask
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


if __name__ == "__main__":
    """ runs the flask app """
    host = '0.0.0.0'
    port = '5000'

    app.run(host=host, port=port, threaded=True)
