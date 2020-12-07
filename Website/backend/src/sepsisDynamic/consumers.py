from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SepsisDynamicConsumer(AsyncJsonWebsocketConsumer):

    groups = ['test']

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
        await self.channel_layer.group_add(
            group='test',
            channel=self.channel_name
        )
        print("THE CHANNEL NAME IS ------------> ", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            group='test',
            channel=self.channel_name
        )
        await super().disconnect(code)

    async def echo_message(self, message):
        await self.send_json({
            'type': message.get('type'),
            'data': message.get('data'),
        })

    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'echo.message':
            await self.send_json({
                'type': message_type,
                'data': content.get('data'),
            })
