# app/home/__init__.py

from flask import Blueprint

home = Blueprint('customer', __name__)

from . import views
