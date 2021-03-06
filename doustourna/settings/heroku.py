import os
import dj_database_url


SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
