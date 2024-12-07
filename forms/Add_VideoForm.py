from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField, EmailField, FileField
from wtforms.validators import DataRequired, Email


# pip install email-validator

class Add_VideoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    file = FileField('Input file', validators=[DataRequired()])
