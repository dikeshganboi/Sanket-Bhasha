import os

# Configure Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "A2SL.settings")

from django.core.wsgi import get_wsgi_application
from vercel_wsgi import handle

# Create the WSGI application
application = get_wsgi_application()

# Vercel entrypoint: wraps the WSGI app for Serverless
# Signature: (event, context) -> response

def handler(event, context):
    return handle(event, context, application)
