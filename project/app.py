# -*- coding: utf-8 -*-

import datetime, logging, os, warnings
from flask import Flask, request, render_template, g

# blueprints
from .auth import *
from .api import *
from .database import *

from logging.handlers import SMTPHandler

from flask.exthook import ExtDeprecationWarning
warnings.simplefilter('ignore', ExtDeprecationWarning)

from .extensions import (db, manager, cache, login)

__all__ = ('create_app', )

BLUEPRINTS = (
	auth,
	api
)

def create_app(config=None, app_name='Proyecto', blueprints=None):
	app = Flask(app_name,
		static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'),
		template_folder="templates"
	)

	app.config.from_pyfile('project/project.config', silent=True)
	app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)

	if blueprints is None:
		blueprints = BLUEPRINTS

	initialize_api()
	blueprints_fabrics(app, blueprints)
	extensions_fabrics(app)
	configure_logging(app)

	return app

def extensions_fabrics(app):
	db.init_app(app)
	manager.init_app(app)
	cache.init_app(app)
	login.init_app(app)

def blueprints_fabrics(app, blueprints):
	"""Configure blueprints in views."""
	for blueprint in blueprints:
		app.register_blueprint(blueprint)

def initialize_api():
	manager.create_api(Postal, 
		methods=['GET'], 
		collection_name="postal_codes", 
		#preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]), 
		postprocessors=dict(GET_SINGLE=[Postal_converter], GET_MANY=[Postals_converter])),
	manager.create_api(Paystat, 
		methods=['GET'], 
		preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]))

def configure_logging(app):
	"""Configure file(info) and email(error) logging."""

	if not app.config['LOG_ENABLED']:
		return

	# Set info level on logger, which might be overwritten by handers.
	# Suppress DEBUG messages.
	app.logger.setLevel(logging.INFO)

	info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
	info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
	info_file_handler.setLevel(logging.INFO)
	info_file_handler.setFormatter(logging.Formatter(
		'%(asctime)s %(levelname)s: %(message)s '
		'[in %(pathname)s:%(lineno)d]')
	)
	app.logger.addHandler(info_file_handler)

	# Testing
	app.logger.info("Testing info.")
	app.logger.warn("Testing warnings.")
	app.logger.error("Testing errors.")