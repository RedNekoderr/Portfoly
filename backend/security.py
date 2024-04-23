from datetime import UTC, datetime, timedelta

import jwt
from config import (ACCESS_TOKEN_EXPIRES, HTTPONLY_ACCESS, HTTPONLY_REFRESH,
                    REFRESH_TOKEN_EXPIRES, SAMESITE, SECRET_KEY, SECURE)
from flask import Blueprint, Response, jsonify, request
from models import Profile, Token, Users, db
from werkzeug.security import check_password_hash, generate_password_hash

security = Blueprint("security", __name__)


def jwt_decode(token: str) -> dict:
    resp: dict
    try:
        resp = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        raise Exception(e)
    return resp


def gen_access_token(user_id: int, username: str) -> str:
    return jwt.encode(
        {
            "id": user_id,
            "user": username,
            "exp": datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRES),
        },
        SECRET_KEY,
        algorithm="HS256",
    )


def gen_refresh_token(user_id: int, username: str) -> str:
    return jwt.encode(
        {
            "id": user_id,
            "user": username,
            "exp": datetime.now(UTC) + timedelta(minutes=REFRESH_TOKEN_EXPIRES),
        },
        SECRET_KEY,
        algorithm="HS256",
    )


def gen_auth_resp(
    access_token: str, refresh_token: str, id: int, username: str
) -> Response:
    resp = jsonify({"auth": True, "id": id, "username": username})
    resp.set_cookie(
        "accessToken",
        access_token,
        httponly=HTTPONLY_ACCESS,
        secure=SECURE,
        samesite=SAMESITE,
    )
    resp.set_cookie(
        "refreshToken",
        refresh_token,
        httponly=HTTPONLY_REFRESH,
        secure=SECURE,
        samesite=SAMESITE,
    )
    return resp


@security.route("/api/decode", methods=["GET"])
def decode() -> tuple[Response, int]:
    token = str(request.args.get("token"))
    try:
        return jsonify(jwt_decode(token)), 200
    except Exception as e:
        return jsonify({"token": f"{e}"}), 403


@security.route("/api/login", methods=["POST"])
def login() -> tuple[Response, int]:
    auth = request.json
    if auth:
        user = Users.query.filter_by(name=auth["username"]).first()
        if user:
            if check_password_hash(user.passwd, auth["password"]):
                try:
                    access_token = gen_access_token(user.id, user.name)
                    refresh_token = gen_refresh_token(user.id, user.name)
                    query = Token.query.filter_by(user_id=user.id)
                    if query:
                        query.update({"refresh": refresh_token})
                    else:
                        t = Token(user_id=user.id, refresh=refresh_token)
                        db.session.add(t)
                    db.session.commit()
                    return (
                        gen_auth_resp(access_token, refresh_token, user.id, user.name),
                        200,
                    )
                except Exception as e:
                    print(e)
                    db.rollback()
    return logout(), 401


@security.route("/api/logout", methods=["GET"])
def logout() -> Response:
    resp = jsonify({"auth": False})
    resp.set_cookie("accessToken", "", expires=1, samesite=SAMESITE)
    resp.set_cookie("refreshToken", "", expires=1, samesite=SAMESITE)
    return resp


@security.route("/api/auth", methods=["GET"])
def auth() -> tuple[Response, int]:
    try:
        access_token = request.cookies.get("accessToken")
        refresh_token = request.cookies.get("refreshToken")

        if not access_token or not refresh_token:
            print("no tokens")
            return logout(), 401

        try:
            access_token_info = jwt_decode(access_token)
            return (
                gen_auth_resp(
                    access_token,
                    refresh_token,
                    access_token_info["id"],
                    access_token_info["user"],
                ),
                200,
            )
        except Exception as e:
            user_id = jwt_decode(refresh_token)["id"]
            query = Token.query.filter_by(user_id=user_id)
            data = query.first()

            if (
                data
                and refresh_token == data.refresh
                and str(e) == "Signature has expired"
            ):
                print("access token expired")
                user = Users.query.filter_by(id=user_id).first()

                if user:
                    access_token = gen_access_token(user.id, user.name)
                    refresh_token = gen_refresh_token(user.id, user.name)
                    query.update({"refresh": refresh_token})
                    db.session.commit()
                    return (
                        gen_auth_resp(access_token, refresh_token, user.id, user.name),
                        200,
                    )
                else:
                    return logout(), 401
            else:
                print("refresh token expired")
                return logout(), 401
    except Exception as e:
        print(e)
        return logout(), 403


@security.route("/api/register", methods=["GET"])
def register() -> tuple[Response, int]:
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        if password and username:
            hash = generate_password_hash(password)
            u = Users(name=username, passwd=hash)
            db.session.add(u)
            db.session.flush()

            access_token = gen_access_token(u.id, u.name)
            refresh_token = gen_refresh_token(u.id, u.name)
            t = Token(user_id=u.id, refresh=refresh_token)
            db.session.add(t)
            db.session.flush()

            p = Profile(user_id=u.id, avatar="default.png", banner="default.png")
            db.session.add(p)

            db.session.commit()
        else:
            raise Exception("Credentials required")
    except Exception as e:
        db.session.rollback()
        return jsonify({"auth": False, "error": f"{e}"}), 403
    return gen_auth_resp(access_token, refresh_token, u.id, u.name), 200
