# -*- coding: utf-8 -*-

from flask import Blueprint

from ..extensions import manager
from ..models import Postal

api = Blueprint('api', __name__)

# FUNCTIONS