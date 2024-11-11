import models
import database


def create_table_for_video():
    db = database.get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS Videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            filename TEXT NOT NULL,
            Foreign key(user_id) references user(id)
        )
    """)


def select_video(video: models.Video):
    db = database.get_db()
    rows = db.execute("SELECT * FROM Video").fetchall()
    return list(map(lambda row: models.Video(*row), rows))


def add_video(video: models.Video):
    db = database.get_db()
    db.execute(
        "insert into Videos (name, user_id, filename) values (?, ?, ?)",
        (video.name, video.user_id, video.filename,)
    )
    db.commit()


def get_videos():
    db = database.get_db()
    rows = db.execute("SELECT * FROM Videos").fetchall()
    return list(map(lambda row: models.Video(*row), rows))


def del_video(video: models.Video):
    db = database.get_db()
    db.execute("DELETE FROM Videos WHERE id = ?", (video.id,))
    db.commit()