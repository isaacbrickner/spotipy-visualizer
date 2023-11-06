from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from app import *

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class TopTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    song_name = db.Column(db.String(100), nullable=False)
    tid = db.Column(db.String(100), unique=True, nullable=False)
    uri = db.Column(db.String(100), unique=True, nullable=False)
    url = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<TopTrack {self.song_name}>"


class TopArtist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    artist_id = db.Column(db.String(100), unique=True, nullable=False)
    genre = db.Column(db.String(150), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<TopArtist {self.artist_name}>"
