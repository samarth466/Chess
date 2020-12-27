"""
Django settings for Chess project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import sys
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g7_x@&4@1=08q5z2s6c27ml4lm+!&27yw=%(9a*ae+_673-t$9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'google_oauth2.apps.GoogleOAuth2Config',
    'rest_framework',
    'tournaments.apps.TournamentsConfig',
    'game.apps.GameConfig',
    'settings.apps.SettingsConfig',
    'UserAuth.apps.UserauthConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'Chess.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if sys.argv[1] == 'test':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'tests/db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'CHESS',
        'USER': 'samarth466',
        'PASSWORD': 'archer_home',
        'HOST': 'localhost',
        'PORT': '1521'
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# additional settings
LOGIN_URL = '/register/'
LOGIN_REDIRECT_URL = '/google/log-in/'
LOGOUT_REDIRECT_URL = '/register/'
#SECURE_SSL_REDIRECT = True
#SECURE_REDIRECT_EXEMPT = [r'^no-ssl/$']
EMAIL_HOST = 'localhost'
#EMAIL_HOST_USER = 'localhost@gameisland.com'
EMAIL_HOST_PASSWORD = 'archer_home'
EMAIL_PORT = 25
SERVER_EMAIL = 'server@gameisland.com'
EMAIL_SUBJECT_PREFIX = '[Django/Gameisland]\n'
EMAIL_USE_LOCALTIME = True
EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'fun.gameisland@gameisland.com'
#SECURE_SSL_REDIRECT = True
LOGGING = {}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'SESSION_ENGINE': 'django.contrib.sessions.backends.cached_db',
        'TIMEOUT': 2419200,
        'VERSION': 1,
        'KEY_PREFIX': 'gameisland.com/'
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
