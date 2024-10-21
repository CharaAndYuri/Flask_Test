from dataclasses import asdict
from random import randint

from flask import Flask, render_template, redirect

from forms.SignUpForm import SignUpForm
from forms.form import GravitationForm
from models import *

users = []
#hello world

def generate_users(n: int):
    for i in range(n):
        age = randint(1, 100)
        user = User(i, "test@example.com", "test", "test surname", age, f"city{i}", "12345")
        users.append(user)


def addUser(email, name, surname, age, city, password):
    if len(users) == 0:
        last_id = 0
    else:
        last_id = max(users, key=lambda x: x.id).id + 1

    user = User(last_id, email, name, surname, age, city, password)
    users.append(user)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/gr_wtf", methods=['GET', 'POST'])
def gr_wtf():
    form = GravitationForm()
    if form.validate_on_submit():
        m1 = form.m1.data
        m2 = form.m2.data
        r = form.r.data

        f = (6 * m1 * m2) / (r ** 2)
        return render_template("gravitation_wtf.html", form=form, output=f)
    return render_template("gravitation_wtf.html", form=form)


@app.route("/signUp", methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        surname = form.surname.data
        age = form.age.data
        city = form.city.data
        password = form.password.data
        confirm_password = form.consfirm_password.data

        if password != confirm_password:
            return render_template(
                "formTemplate.html",
                form=form,
                btn_name="Регистрация!",
                error="Пароли не совпадают!"
            )

        addUser(email, name, surname, age, city, password)
        return redirect("/users")

    return render_template("formTemplate.html", form=form, btn_name="Регистрация!")


@app.route("/users", methods=['GET', 'POST'])
def getUsers():
    return users


@app.route("/users/<int:user_id>")
def getUser(user_id: int):
    for user in users:
        if user.id == user_id:
            return asdict(user)

    return str(None)


@app.route("/delUser/<int:user_id>")
def delUser(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return asdict(user)

    return str(None)


if __name__ == '__main__':
    generate_users(10)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True)
