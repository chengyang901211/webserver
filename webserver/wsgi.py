"""
WSGI config for webserver project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import time
import sys
import signal
import os,sys
sys.path.append('/opt/python/current/app/webserver/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'webserver.settings'


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")

application = get_wsgi_application()
