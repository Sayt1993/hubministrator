from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo