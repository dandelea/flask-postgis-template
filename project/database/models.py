# -*- coding: utf-8 -*-

from ..extensions import db

from geoalchemy2.types import Geometry

class Postal(db.Model):
	__tablename__ = 'postals'
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(5), nullable=False)
	the_geom = db.Column(Geometry, nullable=False)
	paystats = db.relationship('Paystat', backref='area', lazy='dynamic')
	

class Paystat(db.Model):
	__tablename__ = 'paystats'
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	amount = db.Column(db.Float, nullable=False)
	month = db.Column(db.String(10), nullable=False)
	gender = db.Column(db.Enum('F', 'M', name='Gender'), nullable=False)
	age = db.Column(db.Enum('<=24', '25-34', '35-44', '45-54', '55-64',  '>=65', name='Age'), nullable=False)
	postal_id = db.Column(db.Integer, db.ForeignKey('postals.id'), nullable=False)