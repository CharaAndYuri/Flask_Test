import os
from fileinput import filename
from random import randint
from typing import TextIO, IO
from datetime import datetime
from flask_wtf.file import FileField
import static
from flask import Flask, render_template, redirect, request, Response
from flask_login import LoginManager, login_required, login_user, logout_user
import repositories
from forms.Add_VideoForm import Add_VideoForm
from forms.SignUpForm import SignUpForm
from models import *
from repositories import add_video
from forms.SignInForm import SignInForm
from utils import Link



def generate_users(n: int):
    for i in range(n):
        age = randint(1, 100)
        user = User(
            i,
            "test@example.com",
            "".join([chr(randint(73, 89)) for _ in range(randint(5, 15))]),
            age,
            f"city{i}",
            "12345"
        )
        repositories.add_user(user)


def addUser(email, name, age, city, password):
    user = User(None, email, name, age, city, password)
    repositories.add_user(user)


def generate_video():  # Чтение видеофайла поблочно
    with open("path_to_video.mp4", "rb") as video:
        chunk = video.read(1024)
        while chunk:
            yield chunk
            chunk = video.read(1024)

def Add_video(name):
    video = Video(None, name)
    repositories.add_video(video)



app = Flask(__name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return repositories.get_user(user_id)

def save_video(name, file):
    video = Video(None, name, file)
    file.save(name)


@app.route('/video-layout/<filename>')
def video_feed(filename):  # Трансляция видео
    # check file exist
    return Response(generate_video(filename), mimetype='video/mp4')



@app.route('/')
@login_required
def index():
    users = repositories.get_users()
    return render_template(
        'layout/layout.html',
        links=[
            Link("Home", "/"),
            Link("Videos", "/videos"),
            Link("Log out", "/login"),
            Link("Add Video", "/addVideo")
        ],
        users=users
    )


@app.route("/add", methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()

    if form.validate_on_submit():
        email = form.email.data
        name = form.name.data
        age = form.age.data
        city = form.city.data
        password = form.password.data
        confirm_password = form.consfirm_password.data

        if password != confirm_password:
            return render_template(
                "formTemplate.html",
                form=form,
                btn_name="Sign up!",
                error="Passwords don't match!"
            )

        addUser(email, name, age, city, password)
        return redirect("/login")

    return render_template("formTemplate.html", form=form, btn_name="Sign Up!")


@app.route("/addVideo", methods=['GET', 'POST'])
def Add_Video():
    form = Add_VideoForm()

    if form.validate_on_submit():
        name = form.name.data
        file = form.file.data
        filename = (str(datetime.now())
                    .replace(" ", "_")
                    .replace(".", ":")
                    .replace(":", "-")
                    + ".mp4")
        file.save(f"static/{filename}")
        add_video(Video(name=name, user_id=0, id=None, filename=filename))
        return redirect("/")
    return render_template("formTemplate.html", form=form, btn_name="Save video!")

def generate_video(filename):  # Чтение видеофайла поблочно
    with open(f"Static/{filename}", "rb") as video:
        chunk = video.read(1024)
        while chunk:
            yield chunk
            chunk = video.read(1024)

@app.route("/videos", methods=['GET', 'POST'])
def getVideos():
    videos = repositories.get_videos()
    return render_template(
        "videos/list_videos.html",
        videos=videos,
        count=len(videos)
    )


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        users = repositories.get_users()
        for user in users:
            if user.email == email and user.password == password:
                login_user(user)
                return redirect("/")
        return redirect("/login")
    return render_template("formTemplate.html", form=form, btn_name="Login!")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/users/<int:user_id>")
@login_required
def getUser(user_id: int):
    users = repositories.get_users()

    for user in users:
        if user.id == user_id:
            return render_template(
                "layout/user-layout.html",
                links=[
                    Link("Home", "/"),
                    Link("Log out", "/add"),
                  #  Link("Delete User", f"/delUser/{user.id}", class_name="bg-danger"),
                ],
                user=user
            )

    return redirect("/")


@app.route("/delUser/<int:user_id>")
@login_required
def delUser(user_id: int):
    users = repositories.get_users()

    for user in users:
        if user.id == user_id:
            repositories.delete_user(user)

    return redirect("/")


@app.route("/videos/<int:video_id>")
def getVideo(video_id: int):
    videos = repositories.get_videos()

    for video in videos:
        if video.id == video_id:
            return render_template(
                "layout/video-layout.html",
                links=[
                    Link("Home", "/"),
                    Link("Add Video", "/addVideo"),
                  #  Link("Delete Video", f"/delVideo/{video.id}", class_name="bg-danger"),
                ],
                video=video
            )

    return redirect("/")


@app.route("/delVideo/<int:video_id>")
def delVideo(video_id: int):
    videos = repositories.get_videos()

    for video in videos:
        if video.id == video_id:
            repositories.del_video(video)

    return redirect("/")


if __name__ == '__main__':
    login_manager.init_app(app)
    login_manager.unauthorized_handler(lambda : redirect("/login"))
    app.app_context().push()
    repositories.create_table()
    repositories.create_table_for_video()

    #generate_users(1)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port=8080)
