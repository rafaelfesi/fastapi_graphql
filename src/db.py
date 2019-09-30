from typing import Any
from gino import Gino  # type: ignore


db = Gino()
Model: Any = db.Model


class Group(Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class User(Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(None, db.ForeignKey("groups.id"))
    name = db.Column(db.String)
    age = db.Column(db.Integer)


class Address(Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(None, db.ForeignKey("users.id"))
    email_address = db.Column(db.String, nullable=False)


class Details(Model):
    __tablename__ = "details"

    id = db.Column(db.Integer, primary_key=True)
    address_id = db.Column(None, db.ForeignKey("addresses.id"))
    details = db.Column(db.String, nullable=False)
