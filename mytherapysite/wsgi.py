"""
WSGI config for mytherapysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/shayrozen/MyTherapistSite'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'mytherapysite.settings'

# Activate your virtual environment
activate_this = '/home/shayrozen/MyTherapistSite/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
