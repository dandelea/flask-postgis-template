# -*- coding: utf-8 -*-
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from ..extensions import db

class User(db.Model):
    __tablename__ = 'users'
    # tables name convention is contradictory topic, usually I'm against plural forms
    # when name tables, but user is reserved word in post databases,
    # so this is only case when it is allowed to use plural in my teams.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)