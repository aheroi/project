"""
Django settings for the MyFinPages project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import django_heroku
import os

from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'my-f-pages.herokuapp.com'
]


# Application definition

INSTALLED_APPS = [
    # my apps
    'website',
    'myfinpages',
    'accounts',

    # third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap4',
    'crispy_forms',
    'debug_toolbar',
    'django.contrib.sites',
    'django.contrib.humanize',

    # apps by default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'misc.context_processors.add_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa:
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "optional"


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# for translate (?)
LOCALE_PATHS = [BASE_DIR / "locales"]

LANGUAGES = [
    ("en", "English"),
    ("uk", "Ukrainian"),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "public" / "static"
# STATIC_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# for saving media
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Other settings
SITE_ID = 1

INTERNAL_IPS = ['127.0.0.1']

# Emails

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST")

EMAIL_HOST_USER = env("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

EMAIL_PORT = env("EMAIL_PORT")


# django_heroku.settings(locals())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': env('DJANGO_LOG_LEVEL', default='INFO'),
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env('DJANGO_LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
    },
}
