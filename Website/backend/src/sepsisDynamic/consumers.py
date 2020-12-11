from channels.generic.websocket import AsyncJsonWebsocketConsumer
from sepsisAPI.serializers import SepsisPatientSerializer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async


class SepsisDynamicConsumer(AsyncJsonWebsocketConsumer):

    groups = ['test']

    @database_sync_to_async
    def _get_user_group(self, user):
        return user.user_type

    @database_sync_to_async
    def _get_user_user_type_id(self, user):
        """[summary]
        if the user is a doctor then This will give the doctor's model id 
        else it will provide patient's id
        Args:
            user ([type]): The user model
        """
        print("THE USER obj", user.id)
        print("email", user.email)
        if "PATIENT" == _get_user_group(user):
            print("THE PATIENT'S ID ", user.patient_set.values(
                'pat_id'))
            return user.patient_set.values('id')
        elif "DOCTOR" == _get_user_group(user):
            return user.doctor_set.values('id')
        else:
            print("THE USER IS SOMETHING ELSE")

    @database_sync_to_async
    def _created_sepsis_data(self, data):
        print("THE DATA SENT TO DATABASE CHECK USER ID", data)
        x = get_user_model().objects.get(id=data['patient'])
        print("THE USER", x)
        x = x.patient_set.values('id')[0]['id']

        print("THE PATIENT's ID", x)
        # lEts get the user-id of the person which should be converted to the user_patient_id
        # user_id_val = data['patient']
        # print("THE USER id", user_id_val)
        # user_patient_id_val = _get_user_user_type_id(data['user_obj'])
        # data = data.update({'patient': user_patient_id_val})
        print("THE TYPE OF DATA", type(data))
        data.update({'patient': x})
        print("THE NEW DATA", data)
        serializer = SepsisPatientSerializer(data=data)
        print("THE SERIALIZER", serializer)
        serializer.is_valid(raise_exception=True)
        return serializer.create(serializer.validated_data)

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

    async def start_sepsis(self, message):
        data = message.get('data')
        sepsis_generated_and_saved_data = await self._created_sepsis_data(data)
        await self.send_json({
            'type': 'echo.message',
            'data': sepsis_generated_and_saved_data
        })

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
        await self.send_json(message)

    async def receive_json(self, content, **kwargs):
        print("THE RECEIVE FUNCTION RAN")
        message_type = content.get('type')
        print("THE MESSAGE TYPE", message_type)
        if message_type == 'start.sepsis':
            await self.start_sepsis(content)
        if message_type == 'echo.message':
            await self.send_json({
                'type': message_type,
                'data': content.get('data'),
            })
