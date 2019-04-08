"""
Django settings for hackon project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ureka_hy%4-p6#ss$+1h25xjti8#u1=a31r=ufeham(%yj(^t4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

PROJECT_DIR = os.path.dirname(__file__)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'myapp',
    'social_django',
    'admin_auto_filters'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'hackon.urls'

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',
 'social_core.backends.google.GoogleOpenId',
 'social_core.backends.google.GoogleOAuth2', 
 
 'django.contrib.auth.backends.ModelBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect', 
            ],
        },
    },
]

WSGI_APPLICATION = 'hackon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases



# DATABASES = {
#     'default': {         
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd6i181nj6s9jiu',
#         'USER': 'nbjexgcpybsbcc',
#         'PASSWORD': '783ab46b6b511c2cd739494a23271bd16aa9b30c62996a44beb265504f44f779',
#         'HOST': 'ec2-23-23-226-190.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {         
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd861vu0cild97b',
        'USER': 'dtxwhcplztigkd',
        'PASSWORD': '00a8f205ad3514043a629139c9348fd4c3a0dc983a5d77f33fbe0e0abde0ad0d',
        'HOST': 'ec2-54-221-243-211.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#media files

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'






LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/task/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='260489749062-krcm5u7oloejiv6mc1iin3ursvl6lktg.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ZFIyaJtkEBFdaeGzPtUl1cor'





#git add .
#git commit -m "message"
#git push origin google_auth
