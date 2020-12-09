from channels.generic.websocket import AsyncJsonWebsocketConsumer

from channels.db import database_sync_to_async


class SepsisDynamicConsumer(AsyncJsonWebsocketConsumer):

    groups = ['test']

    @database_sync_to_async
    def _get_user_group(self, user):
        return user.user_type

    async def connect(self):
        """[summary]
        • [Understanding of django-channels groups methodology]
            ◘ self.channel_layer.group_add("gossip", self.channel_name) takes
            two arguments: room_name and channel_name
            ◘ When you connect from your browser via socket to this consumer, you are
            creating a new socket connection called as channel. 
            ◘ So, when you open multiple pages in your browser, multiple channels are created. 
            Each channel has a unique Id/name : channel_name
                ♦ The "channel_name" would be provided by django-channel which has to be
                name must be a valid unicode string containing only ASCII with
                alphanumerics, hyphens, underscores, or periods.
            ◘ room is a group of channels. If anyone sends a message to the room, 
            all channels in that room will receive that message.
        """
        print("THE SCOPE is ====> \n", self.scope)
        user = self.scope['user']
        print("\n the user in the consumer \n")
        print("THE USER IS ------>", user)
        print("THE USER IS ANONYMOUS ", user.is_anonymous)

        if user.is_anonymous:
            print("user was unknown")
            await self.close()
        else:
            # ********************* the print statements for authenticated user **************************
            print("\n ---------------------- \n THE SCOPE of user is ====> \n",
                  self.scope['user'])
            print("THE USER GROUP", user.user_type)
            print("IS SUPERUSER", user.is_superuser)
            # ********************************************************************************************
            user_group = await self._get_user_group(user)
            if user_group == 'PATIENT':
                await self.channel_layer.group_add(
                    group='sepis_data_pool',
                    channel=self.channel_name
                )
                await self.accept()

    async def disconnect(self, code):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            user_group = await self._get_user_group(user)
            if user_group == 'PATIENT':
                await self.channel_layer.group_discard(
                    group='sepis_data_pool',
                    channel=self.channel_name
                )
                await super().disconnect(code)

    async def echo_message(self, message):
        print("THE ECHO MESSAGE ALSO RAN")
        await self.send_json({
            'type': message.get('type'),
            'data': message.get('data'),
        })

    async def receive_json(self, content, **kwargs):
        print("THE RECEIVE FUNCTION RAN")
        message_type = content.get('type')
        print("THE MESSAGE TYPE", message_type)
        if message_type == 'echo.message':
            await self.send_json({
                'type': message_type,
                'data': content.get('data'),
            })
