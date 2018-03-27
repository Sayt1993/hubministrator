# app/home/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

from . import home
from ..models import User
from .. import db

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route("/dashboard")
@login_required
def dashboard():
    return render_template('home/dashboard.html', title="Dashboard")


@home.route("/profile/", methods=["GET", "POST"])
@login_required
def show_profile():
    user = User.query.get_or_404(current_user.id)
    return render_template('home/profile.html', user=user, title="User Profile")
