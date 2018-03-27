# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class AdminForm(FlaskForm):
    
    license_m = StringField('License number', validators=[DataRequired()])
    p_iva = StringField('P. iva', validators=[DataRequired()])
    condo_own_n = StringField('condo_own_n', validators=[DataRequired()])

    #condo_fk = db.relationship('Condo', backref='administrators_registry', lazy='dynamic')
    