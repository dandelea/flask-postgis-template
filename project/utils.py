# -*- coding: utf-8 -*-

from .extensions import db

from geoalchemy2.functions import ST_AsGeoJSON

import json, hashlib

def hash(password):
	return hashlib.md5(p.encode('utf8')).hexdigest()

def GeoJSONtoJSON(geojson):
	return json.loads(db.session.scalar(ST_AsGeoJSON(geojson)))