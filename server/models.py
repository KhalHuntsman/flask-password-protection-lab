from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import Schema, fields

from config import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)  # added: private column to store hashed password

    @hybrid_property
    def password_hash(self):
        # added: prevent reading the password hash
        raise AttributeError("Password hashes may not be viewed.")

    @password_hash.setter
    def password_hash(self, password):
        # added: hash plaintext password before storing
        password_bytes = password.encode("utf-8")
        hashed_bytes = bcrypt.generate_password_hash(password_bytes)
        self._password_hash = hashed_bytes.decode("utf-8")

    def authenticate(self, password):
        # added: verify plaintext password against stored hash
        password_bytes = password.encode("utf-8")
        return bcrypt.check_password_hash(
            self._password_hash.encode("utf-8"),
            password_bytes
        )

    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'


class UserSchema(Schema):
    id = fields.Int()
    username = fields.String()
