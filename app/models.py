from . import db
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def get_id(self):
        return self.email