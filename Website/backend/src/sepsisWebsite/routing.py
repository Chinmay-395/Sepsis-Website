from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from sepsisDynamic.consumers import SepsisDynamicConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('sepsisDynamic/', SepsisDynamicConsumer),
    ]),
})
