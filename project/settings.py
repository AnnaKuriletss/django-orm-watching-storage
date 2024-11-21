import os
from environs import Env


env = Env()
env.read_env()


USE_DATABASE = env.bool("USE_DATABASE", default=True)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2" if USE_DATABASE else "",
        "HOST": env("DB_HOST") if USE_DATABASE else "",
        "PORT": env("DB_PORT") if USE_DATABASE else 0,
        "NAME": env("DB_NAME") if USE_DATABASE else "",
        "USER": env("DB_USER") if USE_DATABASE else "",
        "PASSWORD": env("DB_PASSWORD") if USE_DATABASE else "",
    }
}


INSTALLED_APPS = ["datacenter"]

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DEBUG_MODE", default=False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
    },
]

USE_L10N = True

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
