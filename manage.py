# -*- coding: utf-8 -*-

import csv

from flask_script import Manager

from project.auth.models import User
from project.database.models import Postal, Paystat
from project import create_app
from project.extensions import db

manager = Manager(create_app)

@manager.command
def init():
	"""Run in local machine."""
	syncdb()


@manager.command
def syncdb():
	"""Init/reset database."""
	db.drop_all()
	db.create_all()

@manager.command
def restore():
	manager.logger.info('Restore')

	syncdb()

	sources = ('data/paystats.csv', 'data/postal_codes.csv')
	paystats = []
	postal_codes = []

	manager.logger.debug('Start reading data.')

	with open(sources[0], 'rt', encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			paystats.append(row)

	with open(sources[1], 'rt', encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			postal_codes.append(row)

	manager.logger.debug('Start dumping data.')
	
	for postal in postal_codes:
		db.session.add(
			Postal(
				id=postal["id"],
				code=postal["code"],
				the_geom=postal["the_geom"]))

	db.session.commit()

	for paystat in paystats:
		db.session.add(
			Paystat(
				id=paystat["id"],
				postal_id=paystat["postal_code_id"],
				amount=paystat["amount"],
				month=paystat["p_month"],
				age=paystat["p_age"],
				gender=paystat["p_gender"]))

	db.session.commit()

	db.session.add(
		User(
			id=1,
			username="daniel",
			password="daniel"))

	db.session.commit()

	manager.logger.info('SUCCESS')

if __name__ == "__main__":
	manager.run()
