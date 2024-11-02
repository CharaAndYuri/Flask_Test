import models
import database


def create_table():
    db = database.get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)


def add_user(user: models.User):
    db = database.get_db()
    db.execute(
        "insert into Users (email, name, age, city, password) values (?, ?, ?, ?, ?)",
        (user.email, user.name, user.age, user.city, user.password,)
    )
    db.commit()


def get_users():
    db = database.get_db()
    rows = db.execute("SELECT * FROM Users").fetchall()
    return list(map(lambda row: models.User(*row), rows))

def delete_user(user: models.User):
    db = database.get_db()
    db.execute("DELETE FROM Users WHERE id = ?", (user.id,))
    db.commit()
