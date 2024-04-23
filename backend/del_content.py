from os import path, remove

from flask import Blueprint, Response, jsonify, request
from models import Publication, db

del_user_content = Blueprint("del_user_content", __name__)


@del_user_content.route("/api/del/user/publication", methods=["GET"])
def delete_publication() -> tuple[Response, int]:
    id = request.args.get("id")
    try:
        query = Publication.query.get(id)
        if query:
            db.session.delete(query)
            db.session.commit()
            if path.exists(f"./{query.thumbnail}"):
                remove(f"./{query.thumbnail}")

    except Exception as e:
        return jsonify({"message": f"{e}"}), 500
    return jsonify({"message": f"Publication {id} deleted"}), 200
