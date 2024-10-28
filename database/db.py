import sqlite3
import flask
def get_db() -> sqlite3.Connection:
    if "database" in flask.g:
        return flask.g.get("database")
    else:
        connection = sqlite3.connect('database.db')
        flask.g.database = connection
        return connection
def close_db():
    db = flask.g.get("database")
    if db is not None:
        db.close()