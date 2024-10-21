from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email


# pip install email-validator

class SignUpForm(FlaskForm):
    email = EmailField('Электронная почта', validators=[DataRequired(), Email()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия')
    age = IntegerField('Возраст', default=18)
    city = StringField('Город', validators=[DataRequired()])
    gender = SelectField('Пол', choices=[("М", "Мужской"), ("Ж", "Женский")])
    password = PasswordField('Пароль', validators=[DataRequired()])
    consfirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired()])
