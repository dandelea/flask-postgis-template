#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

from flask import json

from flask_script import Manager

from project.auth.models import User
from project.database.models import Postal, Paystat
from project import create_app
from project.extensions import db

from sqlalchemy import MetaData
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.serializer import dumps, loads

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
	print("Start importing data")

	syncdb()

	sources = ('data/paystats.csv', 'data/postal_codes.csv')
	paystats = []
	postal_codes = []
	with open(sources[0], 'rt', encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			paystats.append(row)

	with open(sources[1], 'rt', encoding="utf-8") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			postal_codes.append(row)
	
	for postal in postal_codes:
		db.session.add(
			Postal(
				id=postal["id"],
				code=postal["code"],
				geometry=postal["the_geom"]))

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

	print('Done')

if __name__ == "__main__":
	manager.run()
