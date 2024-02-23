from api.v1.views import app_views
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User
from models import storage


@app_views.route('/token/refresh', methods=['POST'], strict_slashes=False)
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token)
