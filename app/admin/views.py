# app/admin/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import admin
from forms import AdminForm
from .. import db
from ..models import Condo, Condos_Data

@admin.route('/condominiums', methods=['GET', 'POST'])
@login_required
def condominiums_list():
    
    condos_data = get_condo_data()
    
    return render_template('admin/condominiums.html', condos_data=condos_data, title='Condominiums List')


@admin.route('/condominiums/view/<int:id>', methods=['GET', 'POST'])
@login_required
def condominium_view(id):
    
    allowed = False
    condos = get_condo_data()
    
    for condo in condos:
        if(condo.id_condo == id):
            allowed = True
            break
    
    condo_data = Condos_Data.query.filter_by(id_condo=id).first()

    if(allowed):
        return render_template('admin/condominium_view.html', condo_data=condo_data, title='Condominium Details')
    else:
        return render_template('errors/404.html', title='Page not found')

    
def get_condo_data():
    
    ids_condos = []
    condos_data = []
    
    id_admin = current_user.id
    condos = Condo.query.filter_by(id_admin=id_admin).all()
    
    for condo in condos:
        ids_condos.append(condo.id_condo)

    for id_condo in ids_condos:
        condo_data = Condos_Data.query.filter_by(id_condo=id_condo).first()
        condos_data.append(condo_data)
        
    return condos_data




