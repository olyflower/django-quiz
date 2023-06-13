import os

from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = "y=x&59)5q)mg0y05xqi9@*-)nti8e8@b07e2wk@0l$a9+zhh-n"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
