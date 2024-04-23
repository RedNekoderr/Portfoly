from datetime import UTC, datetime

from flask import Blueprint, Response, jsonify, request
from models import Profile, Publication, db
from security import auth

set_user_content = Blueprint("user_conent", __name__)


@set_user_content.route("/api/set/user-info", methods=["POST"])
def set_user_info() -> tuple[Response, int]:
    username = request.form.get("username")
    auth_info = auth()[0].get_json()
    if not auth_info["auth"]:
        return jsonify({"Error": "Update tokens"}), 403
    if username == auth_info["username"]:
        profile = Profile.query.filter_by(user_id=int(auth_info["id"])).first()
        if profile:
            banner_file = request.files.get("banner")
            avatar_file = request.files.get("avatar")
            description = request.form.get("description")
            if banner_file:
                banner_path = f"images/banners/{banner_file.filename}"
                banner_file.save(banner_path)
                profile.banner = banner_file.filename
            if avatar_file:
                avatar_path = f"images/avatars/{avatar_file.filename}"
                avatar_file.save(avatar_path)
                profile.avatar = avatar_file.filename
            if description:
                profile.desc = description
            db.session.commit()
    else:
        print(username, auth_info["username"])

    return (
        jsonify({"auth": True, "User Validation": username == auth_info["username"]}),
        200,
    )


@set_user_content.route("/api/set/user-info/add-publication", methods=["POST"])
def add_publication() -> tuple[Response, int]:
    username = request.form.get("username")
    auth_info = auth()[0].get_json()
    if not auth_info["auth"]:
        return jsonify({"Error": "Authentication failed. Update tokens."}), 403
    if username == auth_info["username"]:
        user = Profile.query.filter_by(user_id=auth_info["id"]).first()
        if user:
            title = request.form.get("title")
            pub_type = request.form.get("pub_type")
            short_desc = request.form.get("short_desc")
            long_desc = request.form.get("long_desc")
            thumbnail_file = request.files.get("thumbnail")
            if title and pub_type and short_desc and thumbnail_file:
                query = (
                    Publication.query.filter_by(user_id=auth_info["id"])
                    .filter_by(title=title)
                    .first()
                )
                if not query:
                    thumbnail_path = f"images/publications/{thumbnail_file.filename}"
                    thumbnail_file.save(thumbnail_path)
                    publication = Publication(
                        user_id=auth_info["id"],
                        title=title,
                        pub_type=pub_type,
                        short_desc=short_desc,
                        desc=long_desc,
                        thumbnail=thumbnail_path,
                        date=datetime.now(UTC),
                    )
                    db.session.add(publication)
                    db.session.commit()
                    return (
                        jsonify(
                            {"auth": True, "User Validation": True, "publication": True}
                        ),
                        201,
                    )
    return jsonify({"Error": "Failed to add publication."}), 400


@set_user_content.route("/api/set/user-info/update-publication", methods=["POST"])
def update_publication() -> tuple[Response, int]:
    username = request.form.get("username")
    auth_info = auth()[0].get_json()
    if not auth_info["auth"]:
        return jsonify({"Error": "Authentication failed. Update tokens."}), 403
    if username == auth_info["username"]:
        user = Profile.query.filter_by(user_id=auth_info["id"]).first()
        if user:

            title = request.form.get("title")
            pub_type = request.form.get("pub_type")
            short_desc = request.form.get("short_desc")
            long_desc = request.form.get("long_desc")
            thumbnail_file = request.files.get("thumbnail")
            id = request.form.get("id")
            if title and pub_type and short_desc and long_desc and id:
                query = Publication.query.get(id)
                if query:
                    if thumbnail_file:
                        thumbnail_path = (
                            f"images/publications/{thumbnail_file.filename}"
                        )
                        thumbnail_file.save(thumbnail_path)
                        query.thumbnail = thumbnail_path
                    query.title = title
                    query.pub_type = pub_type
                    query.short_desc = short_desc
                    query.desc = long_desc
                    db.session.commit()
                    return (
                        jsonify(
                            {"auth": True, "User Validation": True, "publication": True}
                        ),
                        201,
                    )
    else:
        print(username, auth_info["username"])
        return jsonify({"Error": "Failed to update publication."}), 400
    return jsonify({"Error": "Failed to update publication."}), 400
