from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField, EmailField, FileField
from wtforms.validators import DataRequired, Email


# pip install email-validator

class Add_VideoForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    filename = StringField('Имя файла', validators=[DataRequired()])
    file = FileField('Вставьте файл', validators=[DataRequired()])
