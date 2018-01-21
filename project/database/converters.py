# -*- coding: utf-8 -*-

from .models import *

from ..utils import GeoJSONtoJSON

def Postals_converter(filters=None, sort=None, group_by=None, single=None, **kw):
	for object in kw["result"]["objects"]:
		object["the_geom"] = GeoJSONtoJSON(object["the_geom"])
		paystats = object["paystats"]
		total_amount = sum([paystat["amount"] for paystat in paystats])
		object["the_geom"]["properties"]["paystats"] = paystats
		object["the_geom"]["properties"]["total_amount"] = total_amount
		del object["paystats"]

def Postal_converter(filters=None, sort=None, group_by=None, single=None, **kw):
	kw["result"]["the_geom"] = GeoJSONtoJSON(kw["result"]["the_geom"])
	paystats = kw["result"]["paystats"]
	total_amount = sum([paystat["amount"] for paystat in paystats])
	kw["result"]["the_geom"]["properties"]["paystats"] = paystats
	kw["result"]["the_geom"]["properties"]["total_amount"] = total_amount
	del kw["result"]["paystats"]