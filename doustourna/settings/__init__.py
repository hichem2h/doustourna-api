import os

from .base import *

IS_HEROKU = os.environ.get('HOST_ENV') == 'heroku'

if IS_HEROKU:
    from .heroku import *
