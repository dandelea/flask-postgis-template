# -*- coding: utf-8 -*-

from .models import *

from ..utils import GeoJSONtoJSON

def Postals_converter(filters=None, sort=None, group_by=None, single=None, **kw):
	for object in kw["result"]["objects"]:
		object["the_geom"] = GeoJSONtoJSON(object["the_geom"])

def Postal_converter(filters=None, sort=None, group_by=None, single=None, **kw):
	kw["result"]["the_geom"] = GeoJSONtoJSON(kw["result"]["the_geom"])