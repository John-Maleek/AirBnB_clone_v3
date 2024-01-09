#!/usr/bin/python3
"""
    Module defines a Flask Blueprint
"""

from api.v1.views import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
