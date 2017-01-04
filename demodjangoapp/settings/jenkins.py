__author__ = 'ngsee'
from demodjangoapp.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_demodjangoapp',
        'USER': 'scorecard',
        'PASSWORD': 'scorecard_development',
        'HOST': 'qaci01.wic.west.com',
        'PORT': '5433',
    }
}

INSTALLED_APPS += ('django_jenkins', )

PROJECT_APPS = (
    'demodjangoapp.apps.core',
    'demodjangoapp.apps.graphs',
    'demodjangoapp.apps.help',
    'demodjangoapp.apps.projects',
    'demodjangoapp.apps.users'
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
)

TEST_COVERAGE_EXCLUDES_FOLDERS = [
    '/usr/local/*',
    'demodjangoapp/apps/*/tests/*',
]
