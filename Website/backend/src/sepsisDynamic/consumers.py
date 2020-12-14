from channels.generic.websocket import AsyncJsonWebsocketConsumer
from sepsisAPI.serializers import SepsisPatientSerializer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async

from sepsisAPI.models import Patient


class SepsisDynamicConsumer(AsyncJsonWebsocketConsumer):

    groups = ['test']

    # doc_pat_grp_id = ""
    # pat_grp_id = ""

    @database_sync_to_async
    def _get_user_group(self, user):
        return user.user_type

    @database_sync_to_async
    def _get_user_grp_id(self, user):
        """This will return grp_id since django channels' channel-layer requires ASCII unicode as group"""
        print("************** THE grp function initiated **************")
        print("THE USER obj", user)
        print("email", user.email)
        if "PATIENT" == user.user_type:
            return str(user.patient_set.all()[0].grp_id)
        elif "DOCTOR" == user.user_type:
            print("THE patient's unicode ", str(user.doctor_set.all()[
                  0].patient_set.all().values_list('grp_id', flat=True)))
            return map(str, user.doctor_set.all()[0].patient_set.all().values_list('grp_id', flat=True))
        else:
            print("THE USER IS SOMETHING ELSE")

    @database_sync_to_async
    def _get_patient_of_doctor(self, user):
        x = user.doctor_set.all()
        doc_obj = x[0]
        pat_ids = doc_obj.patient_set.all().values_list('grp_id', flat=True)
        return pat_ids

    @database_sync_to_async
    def _created_sepsis_data(self, data):
        """[summary]
            This helper function would generate and return the 
        """
        print("THE DATA SENT TO DATABASE CHECK USER ID", data)
        x = get_user_model().objects.get(id=data['patient'])
        print("THE USER", x)
        x = x.patient_set.values('id')[0]['id']

        print("THE PATIENT's ID", x)

        print("THE TYPE OF DATA", type(data))
        data.update({'patient': x})
        print("THE NEW DATA", data)
        serializer = SepsisPatientSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        x = serializer.create(serializer.validated_data)
        return SepsisPatientSerializer(x).data

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
        # print("THE SCOPE is ====> \n", self.scope)
        user = self.scope['user']
        # print("\n the user in the consumer \n")
        print("THE USER IS ------>", user)
        # print("THE USER IS ANONYMOUS ", user.is_anonymous)

        if user.is_anonymous:
            print("user was unknown")
            await self.close()
        else:
            # ********************* the print statements for authenticated user **************************
            # print("\n ---------------------- \n THE SCOPE of user is ====> \n",
            #       self.scope['user'])
            # print("THE USER GROUP", user.user_type)
            # print("IS SUPERUSER", user.is_superuser)
            # ********************************************************************************************
            # user_group = await self._get_user_group(user)
            if user.user_type == 'PATIENT':
                self.pat_grp_id = await self._get_user_grp_id(user)
                await self.channel_layer.group_add(
                    group=self.pat_grp_id,
                    channel=self.channel_name
                )
                print("CONNECT TO ---------> ", self.pat_grp_id)

            elif user.user_type == 'DOCTOR':
                # to check which patient is online
                print("THE DOC CONDITION RAN")
                for self.doc_pat_grp_id in await self._get_user_grp_id(user):
                    print("Doc connected --------->", self.doc_pat_grp_id)
                    await self.channel_layer.group_add(
                        group=self.doc_pat_grp_id,
                        channel=self.channel_name
                    )
                print("Doc connected ", self.doc_pat_grp_id)
            await self.accept()

    async def start_sepsis(self, message):
        data = message.get('data')
        sepsis_generated_and_saved_data = await self._created_sepsis_data(data)
        await self.channel_layer.group_send(
            group=self.pat_grp_id,
            message={
                'type': 'echo.message',
                'data': sepsis_generated_and_saved_data
            }
        )
        # await self.send_json({
        #     'type': 'echo.group_message',
        #     'data': sepsis_generated_and_saved_data
        # })

    async def disconnect(self, code):
        user = self.scope['user']
        if user.is_anonymous:
            await self.close()
        else:
            if user.user_type == 'PATIENT':
                pat_grp_id = await self._get_user_grp_id(user)
                await self.channel_layer.group_discard(
                    group=pat_grp_id,
                    channel=self.channel_name
                )
                await super().disconnect(code)

    async def echo_message(self, message):
        print("THE ECHO MESSAGE ALSO RAN")
        await self.send_json(message)

    async def echo_group_message(self, message):
        print("THE MESSAGE", message)
        print("THE USER THAT CALLED the echo-group-function is",
              self.scope['user'])
        content = message.get('data')
        print("THE CONTENTS ARE ", content)
        if self.scope['user'].user_type == 'PATIENT':
            print("THE patient grp_id is", self.pat_grp_id)
            await self.channel_layer.group_send(
                group=self.pat_grp_id,
                message={
                    "type": "echo.message",
                    "data": message.get('data')
                }
            )
        elif self.scope['user'].user_type == 'DOCTOR':
            print("THE doctor grp_id is", self.doc_pat_grp_id)
            await self.channel_layer.group_send(group=self.doc_pat_grp_id,
                                                message={
                                                    'type': 'echo.message',
                                                    'data': content
                                                }
                                                )

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
        if message_type == 'echo.group_message':
            await self.echo_group_message(content)
