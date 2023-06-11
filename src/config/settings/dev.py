import os

from config.settings.base import *  # noqa

DEBUG = True

SECRET_KEY = "uKSug2etxXWtLkPsAzzGKn6qxHQDAkYR7mM5Euj84Smm"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
