"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import environ
import os

import django_heroku

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from environs import Env # new
env = Env() # new
env.read_env() # new

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("MY_SECRET_KEY") # 'django-insecure-fkw=p&c6t0ujih0p9^l0ys3ry77sbn)o-73z#!c&1y6k4nprr9'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#DEBUG = False
DEBUG =  False #env.bool("MY_DEBUG", default=False)
PREPEND_WWW = True
BASE_URL = "https://vinetcepage.herokuapp.com"
#https://vinetcepage.herokuapp.com/
ALLOWED_HOSTS = ['vinetcepage.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # new
    'django.contrib.staticfiles',


    # mid
   
    'debug_toolbar',
    'cloudinary',
    'ckeditor',
    "crispy_forms",
    #"crispy_bootstrap5",

    #
    'accounts',
    'pages',
    'vins',
]

AUTH_USER_MODEL = 'accounts.CustomUser' # new


#CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap4"


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'lvcloud',
    'API_KEY': '144646879732624',
    'API_SECRET': 'jAdj2Wc2Qb6fmJfY9qJXdEMUYSw',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # new

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'vins_plus': 'templatetags.vins_plus',
            }
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASES = {
    "default": env.dj_db_url("MY_DATABASE_URL")
}
'''

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))] #os.path.join(BASE_DIR,'static')
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles')) # new
STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage' # new

MEDIA_URL = '/media/'


MEDIA_ROOT = [str(BASE_DIR.joinpath('media'))]



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# Needed for 3.2 and later
# https://stackoverflow.com/questions/67783120/warning-auto-created-primary-key-used-when-not-defining-a-primary-key-type-by
#DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'home' # new
LOGOUT_REDIRECT_URL = 'home' # new



#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'your_custom_email_account'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'sendgrid_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True



# Django resize
DJANGORESIZED_DEFAULT_SIZE = [300, 300]
DJANGORESIZED_DEFAULT_CROP = ['middle', 'center']
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'PNG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'PNG': ".png"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True



# Heroku 

django_heroku.settings(locals())

#https://github.com/jacobian/dj-database-url/issues/107
#del DATABASES['default']['OPTIONS']['sslmode']