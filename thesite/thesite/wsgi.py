"""
WSGI config for thesite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


import os
import sys

# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/ppsite/thesite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'thesite.settings'

# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()