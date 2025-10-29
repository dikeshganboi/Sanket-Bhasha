import os

# Configure Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "A2SL.settings")

from django.core.wsgi import get_wsgi_application

# Export a WSGI application as `app`.
# Vercel Python runtime can serve WSGI apps directly when exposed as `app`.
app = get_wsgi_application()
