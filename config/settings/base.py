import os

import environ
from django.utils.translation import ugettext_lazy as _

BASE_DIR = environ.Path(__file__) - 3  # type: environ.Path

env = environ.Env()
env.read_env(BASE_DIR('.env'))

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

EMAIL_CONFIG = env.email_url('DJANGO_EMAIL_URL', default='consolemail://')
vars().update(EMAIL_CONFIG)
SERVER_EMAIL = EMAIL_CONFIG['EMAIL_HOST_USER']
DEFAULT_FROM_EMAIL = SERVER_EMAIL

DATABASES = {'default': env.db("DATABASE_URL")}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.humanize',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_framework_docs',
    'rest_framework_swagger',

    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR("templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MEDIA_ROOT = BASE_DIR('media')
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR('static-collected')
STATIC_URL = '/static/'

FILE_UPLOAD_PERMISSIONS = 0o644

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
