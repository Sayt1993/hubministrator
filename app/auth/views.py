# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User, Administrator_Registry

@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    category = form.category.data

    is_admin = False
    is_resident = False
    is_provider = False

    if category == "admin":
        is_admin = True
    elif category == "resident":
        is_resident = True
    elif category == "provider":
        is_provider = True

    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
            is_admin = is_admin,
            is_resident = is_resident,
            is_provider = is_provider)

        db.session.add(user)
        db.session.commit()

        administrator_registry = Administrator_Registry(
            id_usr = User.query.filter_by(email=user.email).first().id,
            license_n = "prova",
            p_iva = "prova",
            condo_own_n = 11
        )
        db.session.add(administrator_registry)
        db.session.commit()

        flash('You have successfully registered! You may now login.')

    return render_template("auth/register.html", form=form, title='Register')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("home.dashboard"))
        else:
            flash('Invalid email or password.')

    return render_template("auth/login.html", form=form, title='Login')


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for("auth.login"))