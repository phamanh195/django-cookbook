"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import sys
import environ
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.versioning import get_git_changeset_timestamp


environ.Env.read_env('environment.env')


def get_secret(setting):
    """Get the secret variable or return explicit exception"""
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = f'Set the {setting} environment variable'
        raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXTERNAL_BASE = os.path.join(BASE_DIR, 'externals')
EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, 'libs')
EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, 'apps')

sys.path = ['', EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myproject.apps.core',
    'myproject.apps.categories',
    'myproject.apps.ideas',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'myproject', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOCALE_PATH = [
    os.path.join(BASE_DIR, 'locale'),
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'myproject', 'site_static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('DATABASE_NAME'),
        'USER': get_secret('DATABASE_USER'),
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ("bg", "Bulgarian"),    ("hr", "Croatian"),
    ("cs", "Czech"),        ("da", "Danish"),
    ("nl", "Dutch"),        ("en", "English"),
    ("et", "Estonian"),     ("fi", "Finnish"),
    ("fr", "French"),       ("de", "German"),
    ("el", "Greek"),        ("hu", "Hungarian"),
    ("ga", "Irish"),        ("it", "Italian"),
    ("lv", "Latvian"),      ("lt", "Lithuanian"),
    ("mt", "Maltese"),      ("pl", "Polish"),
    ("pt", "Portuguese"),   ("ro", "Romanian"),
    ("sk", "Slovak"),       ("sl", "Slovene"),
    ("es", "Spanish"),      ("sv", "Swedish"),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

timestamp = get_git_changeset_timestamp(BASE_DIR)
STATIC_URL = f'/static/{timestamp}/'


MAGAZINE_ARTICLE_THEME_CHOICES = [
    ('futurism', _("Futurism")),
    ('nostalgia', _("Nostalgia")),
    ('sustainability', _("Sustainability")),
    ('wonder', _("Wonder")),
    ('positivity', _("Positivity")),
    ('solutions', _("Solutions")),
    ('science', _("Science")),
]
