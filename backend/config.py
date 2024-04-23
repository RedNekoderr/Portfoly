from os import getenv

SECRET_KEY = getenv("SECRET_KEY")
DEBUG = False
SECURE = not DEBUG
HTTPONLY_ACCESS = False
HTTPONLY_REFRESH = True
SAMESITE = "strict"
SQLDB = "sqlite:///test.db"
CORS_ORIGINS = ["http://localhost:5173"]
ACCESS_TOKEN_EXPIRES = 30
REFRESH_TOKEN_EXPIRES = 21600
