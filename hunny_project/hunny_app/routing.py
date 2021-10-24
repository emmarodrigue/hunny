from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/hunny_app/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]