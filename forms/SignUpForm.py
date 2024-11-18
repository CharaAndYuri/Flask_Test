from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email


# pip install email-validator

class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname')
    age = IntegerField('Age', default=18)
    city = StringField('Sity', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[("M", "Male"), ("F", "Female"), ("A", "Another") ])
    password = PasswordField('Password', validators=[DataRequired()])
    consfirm_password = PasswordField('Confirm password', validators=[DataRequired()])
