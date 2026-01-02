#!/usr/bin/env python3
# Author: Hunter
# Date: 2026-01-02
# Version: 1.0

from flask import session, request
from flask_restful import Resource

from config import app, api, db
from models import User, UserSchema

user_schema = UserSchema()


class Signup(Resource):
    def post(self):
        data = request.get_json()

        user = User(username=data["username"])
        user.password_hash = data["password"]

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201


class Login(Resource):
    def post(self):
        data = request.get_json()

        user = User.query.filter(User.username == data["username"]).first()

        if user and user.authenticate(data["password"]):
            session["user_id"] = user.id
            return user_schema.dump(user), 200

        return {"error": "Invalid username or password"}, 401


class Logout(Resource):
    def delete(self):
        session.pop("page_views", None)
        session.pop("user_id", None)
        return {}, 204


class CheckSession(Resource):
    def get(self):
        user_id = session.get("user_id")
        if user_id:
            user = User.query.get(user_id)
            return user_schema.dump(user), 200
        return {}, 204


api.add_resource(Signup, "/signup", endpoint="signup")
api.add_resource(Login, "/login", endpoint="login")
api.add_resource(Logout, "/logout", endpoint="logout")
api.add_resource(CheckSession, "/check_session", endpoint="check_session")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
