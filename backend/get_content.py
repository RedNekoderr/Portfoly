from flask import Blueprint, Response, jsonify, request, send_file
from models import Profile, Publication, Users

get_user_content = Blueprint("get_user_content", __name__)


def get_user_info(username: str | None, query_type: str, default_url: str) -> Response:
    try:
        query_id = Users.query.filter_by(name=username).first()
        if query_id:
            query_result = Profile.query.filter_by(user_id=query_id.id).first()
            if query_result:
                match query_type:
                    case "avatar":
                        return send_file(
                            f"images/avatars/{query_result.avatar}",
                            mimetype="image/png",
                        )
                    case "banner":
                        return send_file(
                            f"images/banners/{query_result.banner}",
                            mimetype="image/png",
                        )
        return send_file(default_url, mimetype="image/png")
    except Exception:
        return send_file(default_url, mimetype="image/png")


@get_user_content.route("/api/get-info/user/avatar", methods=["GET"])
def get_user_avatar() -> Response:
    username = request.args.get("username")
    return get_user_info(username, "avatar", "images/avatars/default.png")


@get_user_content.route("/api/get-info/user/banner", methods=["GET"])
def get_user_banner() -> Response:
    username = request.args.get("username")
    return get_user_info(username, "banner", "images/banners/default.jpg")


@get_user_content.route("/api/get-info/user/publications", methods=["GET"])
def get_user_publications() -> tuple[Response, int]:
    username = request.args.get("username")
    user_request = Users.query.filter_by(name=username).first()
    if user_request and user_request.id:
        user = Profile.query.filter_by(user_id=user_request.id).first()
        if user and user.id:
            publications = Publication.query.filter_by(user_id=user.id).all()
            return (
                jsonify(
                    {
                        "publications": [
                            publication.to_dict() for publication in publications
                        ]
                    }
                ),
                200,
            )
    return jsonify({"Error": "User not found."}), 404


@get_user_content.route("/api/get-info/publication-thumbnail", methods=["GET"])
def get_publication_thumbnail() -> tuple[Response, int]:
    try:
        publication_id = request.args.get("id")
        publication = Publication.query.filter_by(id=publication_id).first()
        if publication and publication.thumbnail:
            return send_file(publication.thumbnail, mimetype="image/png"), 200
        return send_file("images/publications/default.png", mimetype="image/png"), 200
    except Exception:
        return send_file("images/publications/default.png", mimetype="image/png"), 200


@get_user_content.route("/api/get-info/users", methods=["GET"])
def get_user_list() -> tuple[Response, int]:
    response = []
    users = Users.query.all()
    for user in users:
        profile = Profile.query.filter_by(user_id=user.id).first()
        if profile:
            response.append({"username": user.name, "avatar": profile.avatar})
    return jsonify(response), 200


@get_user_content.route("/api/get-info/publications/latest", methods=["GET"])
def get_latest_publications() -> tuple[Response, int]:
    response = []
    publications = Publication.query.order_by(Publication.id.desc()).all()
    for publication in publications:
        user = Users.query.filter_by(id=publication.user_id).first()
        profile = Profile.query.filter_by(user_id=publication.user_id).first()
        if user and profile:
            response.append(
                {
                    **publication.to_dict(),
                    "username": user.name,
                    "avatar": profile.avatar,
                }
            )
    return jsonify(response[:4]), 200


@get_user_content.route("/api/get-info/user/description", methods=["GET"])
def get_user_description() -> tuple[Response, int]:
    username = request.args.get("username")
    user = Users.query.filter_by(name=username).first()
    if user and user.id:
        profile = Profile.query.filter_by(user_id=user.id).first()
        if profile and profile.desc:
            return jsonify({"desc": profile.desc}), 200
    return jsonify({"Error": "User not found."}), 404
