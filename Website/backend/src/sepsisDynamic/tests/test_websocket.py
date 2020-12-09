import pytest
from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from sepsisWebsite.routing import application


TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}


@database_sync_to_async
def create_user(email, password, name="Ahamad"):
    user = get_user_model().objects.create_user(
        email=email,
        name=name,
        password=password,
        user_type="PATIENT"
    )
    user.save()
    token, created = Token.objects.get_or_create(
        user=user)
    access = token  # Token.key #for_user(user)
    return user, access


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
class TestWebSocket:
    async def test_can_connect_to_server(self, settings):
        """[summary]
        • This test will send the will create a variable called
        `communicator` which would call the consumer of SepsisDynamic
        • The `communicator` will call the inbuild `connect` 
        function of Django-Channels to send a connection establishment request 
        """
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        _, access = await create_user(
            'test.user@example.com', 'pAssw0rd'
        )
        communicator = WebsocketCommunicator(
            application=application,
            path=f'/sepsisDynamic/?token={access}'
        )
        connected, _ = await communicator.connect()
        assert connected is True
        await communicator.disconnect()

    async def test_can_send_and_receive_messages(self, settings):
        """[summary]
        • Once the connection established we will send a json data
        using the inbuild function of django-Channels called `send_json_to` 
        with the json(data) of `type` & `data` as their key.
        The `Type` ---> would determine which function to call
        The `Data` ---> would be the actual data
        • If the data has been sent succesfully, the function(described in `Type`)
        would return some json data which would captured by
        `receive_json_from` inbuilt function of django-channels
        """
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        _, access = await create_user(
            'test.user@example.com', 'pAssw0rd'
        )
        communicator = WebsocketCommunicator(
            application=application,
            path=f'/sepsisDynamic/?token={access}'
        )
        connected, _ = await communicator.connect()
        message = {
            'type': 'echo.message',
            'data': 'This is a test message.',
        }
        await communicator.send_json_to(message)
        response = await communicator.receive_json_from()
        assert response == message
        await communicator.disconnect()

    # async def test_can_send_and_receive_broadcast_messages(self, settings):
    #     """[Note]
    #     • the `channel layer` is used to broadcast a message to a group.
    #     Whereas the last test modeled a user talking to himself in an empty room,
    #     this most recent test represents a user talking to a room full of people.
    #     """
    #     """[summary]
    #     In this we are using channel-layer and groups to send & receive
    #     broadcasted data; this is very similar to upper test.
    #     """
    #     settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
    #     _, access = await create_user(
    #         'test.user@example.com', 'pAssw0rd'
    #     )
    #     communicator = WebsocketCommunicator(
    #         application=application,
    #         path=f'/sepsisDynamic/?token={access}'
    #     )
    #     connected, _ = await communicator.connect()
    #     message = {
    #         'type': 'echo.message',
    #         'data': 'This is a test message.',
    #     }
    #     channel_layer = get_channel_layer()
    #     await channel_layer.group_send('test', message=message)
    #     response = await communicator.receive_json_from()
    #     assert response == message
    #     await communicator.disconnect()

    async def test_cannot_connect_to_socket(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        communicator = WebsocketCommunicator(
            application=application,
            path='/sepsisDynamic/'
        )
        connected, _ = await communicator.connect()
        assert connected is False
        await communicator.disconnect()

    async def test_join_sepsis_pool(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        _, access = await create_user(
            'test.user@example.com', 'pAssw0rd', 'driver'
        )
        communicator = WebsocketCommunicator(
            application=application,
            path=f'/sepsisDynamic/?token={access}'
        )
        connected, _ = await communicator.connect()
        message = {
            'type': 'echo.message',
            'data': 'This is a test message.',
        }
        channel_layer = get_channel_layer()
        await channel_layer.group_send('sepis_data_pool', message=message)
        response = await communicator.receive_json_from()
        assert response == message
        await communicator.disconnect()
