# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, IntegerField, StringField, SubmitField, SelectField, ValidationError, DateField
from wtforms.validators import DataRequired, Email, EqualTo


class CondoDetailsForm(FlaskForm):
    condo_name = StringField('Nome condominio')
    condo_age = DateField('Data di registrazione')
    cf_c = StringField('C.F.')
    city = StringField('Citta')
    district = StringField('Quartiere')
    address = StringField('Indirizzo')
    house_n = IntegerField('N. di interni')
    condo_n = IntegerField('N. di condomini')
    stair_n = IntegerField('Scale')
    flat_n = IntegerField('Appartamenti')
    cap = IntegerField('Cap')
    submit = SubmitField('Salva')
