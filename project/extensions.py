# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import flask_restless
manager = flask_restless.APIManager(flask_sqlalchemy_db=db)

from flask_cache import Cache
cache = Cache()

from flask_jwt import JWT, jwt_required
login = JWT()