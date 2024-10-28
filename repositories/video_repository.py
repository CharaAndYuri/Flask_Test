import models
import database

def create_table_for_video():
    db = database.get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS Video (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            file_name TEXT NOT NULL,
            Foreign key(user_id) references user(id)
        )
    """)


def select_video(video: models.Video):
    db = database.get_db()
    rows = db.execute("SELECT * FROM Video").fetchall()
    return list(map(lambda row: models.Video(*row), rows))


def delete_video(video: models.Video):
    db = database.get_db()
    db.execute("DELETE FROM Users WHERE id = ?", (video.id))
