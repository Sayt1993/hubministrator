# app/admin/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import admin
from forms import AdminForm
from .. import db
from ..models import Condo

@admin.route('/condominiums')
@login_required
def condominiums_list():
    """
    List all roles
    """
    condos = Condo.query.all()
    return render_template('admin/condominiums.html',
                           condos=condos, title='Condominiums List')