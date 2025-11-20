"""Minimal Django settings for the freight gateway demo."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET', 'dev-secret')
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'gateway',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'freight_gateway.urls'

TEMPLATES = []

WSGI_APPLICATION = 'freight_gateway.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
