# app/admin/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from . import admin
from forms import CondoDetailsForm
from .. import db
from ..models import Condo, Condos_Data, User, Administrator_Registry

#LIST

@admin.route('/condominiums', methods=['GET', 'POST'])
@login_required
def condominiums_list():

    admin_check = check_admin()
    condos_data = get_condo_data()

    return render_template('admin/condominiums.html', condos_data=condos_data, title='Condominiums List')

#SELECT

@admin.route('/condominiums/view/<int:id>', methods=['GET', 'POST'])
@login_required
def condominium_view(id):

    admin_check = check_admin()
    condos = get_condo_data()
    is_allowed = check_condo_for_admin(id)

    condo_data = Condos_Data.query.filter_by(id_condo=id).first()

    if(is_allowed):
        return render_template('admin/condominium_view.html', condo_data=condo_data, title='Condominium Details')
    else:
        return render_template('errors/404.html', title='Page not found')

#UPDATE

@admin.route('/condominiums/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def condominium_edit(id):

    admin_check = check_admin()
    condos = get_condo_data()
    is_allowed = check_condo_for_admin(id)

    condos_data = Condos_Data.query.get_or_404(id)

    form = CondoDetailsForm(obj = condos_data)

    if form.validate_on_submit():

        condos_data.condo_name = form.condo_name.data,
        condos_data.condo_age = form.condo_age.data,
        condos_data.cf_c = form.cf_c.data,
        condos_data.city = form.city.data,
        condos_data.district = form.district.data,
        condos_data.address = form.district.data,
        condos_data.house_n = form.house_n.data,
        condos_data.condo_n = form.condo_n.data,
        condos_data.stair_n = form.stair_n.data,
        condos_data.flat_n = form.flat_n.data,
        condos_data.cap = form.cap.data,

        db.session.commit()
        flash('The condominium details have been succesfully modified')

    if(is_allowed):
        return render_template('admin/condominium_edit.html', form=form, title='Condominium edit')
    else:
        return render_template('errors/404.html', title='Page not found')

#INSERT

@admin.route('/condominiums/add', methods=['GET', 'POST'])
@login_required
def condominium_add():

    admin_check = check_admin()
    form = CondoDetailsForm()

    if form.validate_on_submit():

        admin = Administrator_Registry.query.filter_by(id_usr=current_user.id).first()

        condo = Condo(
            condo_name = form.condo_name.data,
            id_admin = admin.id_admin
        )

        db.session.add(condo)
        db.session.commit()

        condo_fk = Condo.query.filter_by(condo_name=form.condo_name.data, id_admin = current_user.id).first()
        condo_data = Condos_Data(
            condo_name = form.condo_name.data,
            condo_age = form.condo_age.data,
            cf_c = form.cf_c.data,
            city = form.city.data,
            district = form.district.data,
            address = form.district.data,
            house_n = form.house_n.data,
            condo_n = form.condo_n.data,
            stair_n = form.stair_n.data,
            flat_n = form.flat_n.data,
            cap = form.cap.data,
            id_condo = condo_fk.id_condo
        )

        db.session.add(condo_data)
        db.session.commit()

        flash('You have successfully added a condo.')

        return redirect(url_for("admin.condominiums_list"))

    if(admin_check):
        return render_template('admin/condominium_add.html', form=form, title='Condominium list')
    else:
        return render_template('errors/404.html', title='Page not found')


#funzione per delete


def check_condo_for_admin(id):

    allowed = False
    condos = get_condo_data()

    for condo in condos:
        if(condo.id_condo == id):
            allowed = True
            break

    return allowed

def check_admin():
    user = User.query.filter_by(id_usr=current_user.id).first()
    if(user.is_admin):
        return True
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




