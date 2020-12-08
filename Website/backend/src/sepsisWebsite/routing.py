from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
# from sepsisWebsite.middleware import TokenAuthMiddlewareStack
from channels.auth import AuthMiddlewareStack
from sepsisWebsite.middleware import TokenAuthMiddlewareStack
from sepsisDynamic.consumers import SepsisDynamicConsumer

# application = ProtocolTypeRouter({
#     'websocket': TokenAuthMiddlewareStack(
#         URLRouter([
#             path('sepsisDynamic/', SepsisDynamicConsumer),
#         ]),
#     ),
# })
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('sepsisDynamic/', SepsisDynamicConsumer),
    ]),
})
