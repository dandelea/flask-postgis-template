# -*- coding: utf-8 -*-

from ..extensions import login
from .models import User

from flask import Blueprint
from flask_jwt import jwt_required

auth = Blueprint('auth', __name__, url_prefix='/auth/')

# FUNCTIONS

@login.authentication_handler
def authenticate(username, password):
	user = User.query.filter_by(username=username).first()
	# Assumes the password comes hashed from client.
	if user != None and user.password == password:
		return user
	return None

@login.identity_handler
def load_user(payload):
	user = User.query.filter_by(id=payload['identity']).first()
	return user

@jwt_required()
def auth_func(*args, **kw):
	return True