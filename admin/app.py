#!/usr/bin/python3
""" Flask app for manipulating admin panel """
from flask import Flask
from flask_admin import Admin
from models.user import User
from models import storage
from flask_admin.contrib.sqla import ModelView
import uuid

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
app.config['SECRET_KEY'] = 'mysecret_key'

class UserAdmin(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            # This is a new record being created
            model.id = str(uuid.uuid4())

admin = Admin(app, name='Admin Panel')

# Register the User model with the same admin instance
admin.add_view(UserAdmin(User, storage.session))

if __name__ == '__main__':
    """ runs Flask app """
    app.run(host='0.0.0.0', port=5001, threaded=True, debug=True)
