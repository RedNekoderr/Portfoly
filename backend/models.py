from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True, nullable=False)
    passwd = db.Column(db.String(512), nullable=False)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    banner = db.Column(db.String(512), default="")
    avatar = db.Column(db.String(512), default="")
    desc = db.Column(db.String(256), default="")


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    refresh = db.Column(db.String(512), default="")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    pub_type = db.Column(db.String(3), nullable=False)
    short_desc = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(db.String(512), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "pub_type": self.pub_type,
            "short_desc": self.short_desc,
            "desc": self.desc,
            "thumbnail": self.thumbnail,
            "date": self.date,
            "blob": "images/default-publication.png",
        }
