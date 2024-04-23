from config import CORS_ORIGINS, SECRET_KEY, SQLDB
from del_content import del_user_content
from flask import Flask
from flask_cors import CORS
from get_content import get_user_content
from models import db
from security import security
from set_content import set_user_content

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLDB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
for blueprint in (set_user_content, get_user_content, del_user_content, security):
    app.register_blueprint(blueprint)

cors = CORS(
    app,
    resources={r"*": {"origins": CORS_ORIGINS}},
    supports_credentials=True,
)


@app.before_request
def create_tables() -> None:
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    if SECRET_KEY:
        app.run()
