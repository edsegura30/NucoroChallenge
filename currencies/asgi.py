# Pip imports
from channels.routing import ProtocolTypeRouter

# Python imports
import os

# Internal imports
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currencies.settings')


django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        # We can add more protocols here, but for the scope HTTP works just fine
        "http": django_asgi_application,
    }
)