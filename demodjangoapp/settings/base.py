import os
import sys
import ldap
import pytz
import django.conf.global_settings as DEFAULT_SETTINGS

from django_auth_ldap.config import LDAPSearch

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
root = lambda *x: os.path.join(BASE_DIR, *x)

sys.path.insert(0, root('apps'))

DEBUG = True
TEMPLATE_DEBUG = True 

MEDIA_ROOT = os.environ.get('MEDIA_ROOT')

LOGIN_URL = '/demodjangoapp/'

BROKER_URL = os.environ.get('RABBITMQ_URL')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#hw547!xqjvn@%1^jz+6os8u=dfr8dom==!%rs)53&m%og9wo@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

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
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_auth_ldap.backend.LDAPBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://10.27.116.51"
AUTH_LDAP_BIND_DN = "cn=LDAP Query\\, Domino Server, OU=Service Accounts,DC=corp,DC=westworlds,DC=com"
AUTH_LDAP_BIND_PASSWORD = "Qu3ryLd@p"
AUTH_LDAP_USER_SEARCH = LDAPSearch('DC=corp,DC=westworlds,DC=com',
    ldap.SCOPE_SUBTREE, "(samaccountname=%(user)s)")

AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenname',
    'last_name': 'sn',
    'email': 'mail'
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demodjangoapp',
]

PROJECT_APPS = []

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demodjangoapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'demodjangoapp.wsgi.application'

# Database

# import dj_database_url
# DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'demodjangoapp',
        'USER': 'demo',
        'PASSWORD': 'demo',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
   0: 'default',
   15: 'primary',
   35: 'danger',
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.environ.get('STATIC_ROOT')
STATIC_URL = '/static/'


# Additional locations of static files

# Password validation

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


# .local.py overrides all the common settings.
try:
    from .local import *  
except ImportError:
    pass

# Celery config
CELERY_ACCEPT_CONTENT = ['pickle', 'json', ]
CELERY_TIMEZONE = pytz.timezone('US/Central')
CELERY_ENABLE_UTC = False
CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_SERIALIZER = 'pickle'