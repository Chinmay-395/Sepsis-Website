from channels.generic.websocket import AsyncJsonWebsocketConsumer
from sepsisAPI.serializers import SepsisPatientSerializer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

from sepsisAPI.models import Patient

import random
import time
import json
import asyncio


class SepsisDynamicConsumer(AsyncJsonWebsocketConsumer):

    groups = ['test']

    @database_sync_to_async
    def _get_user_grp_id(self, user):
        """This will return grp_id since django channels' channel-layer requires ASCII unicode as group"""
        # print("************** THE grp function initiated **************")
        print("THE USER obj", user)
        print("email", user.email)
        if "PATIENT" == user.user_type:
            return str(user.patient_set.all()[0].grp_id)
        elif "DOCTOR" == user.user_type:
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
    def _convert_user_id_to_patient_id(self, data):
        if (str(self.scope['user'].user_type) == 'PATIENT' and self.scope['user'].id == data['patient']):
            x = get_user_model().objects.get(id=data['patient'])
            x = x.patient_set.values('id')[0]['id']
            data.update({'patient': x})
            return data

    # the following code is important
    @database_sync_to_async
    def serializer_checking_saving_data(self, data):
        serializer = SepsisPatientSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        x = serializer.create(serializer.validated_data)
        serializer.save()
        return SepsisPatientSerializer(x).data

    async def connect(self):
        """
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
        user = self.scope['user']
        if user.is_anonymous:
            print("user was unknown")
            await self.close()
        else:
            self.room_group_name = await self._get_user_grp_id(user)
            if user.user_type == 'PATIENT':
                self.pat_grp_id = await self._get_user_grp_id(user)
                await self.channel_layer.group_add(
                    group=self.pat_grp_id,
                    channel=self.channel_name
                )
                print(
                    f"THE CHANNEL NAME for PATIENT ---------> {self.channel_name}")
                print("Patient GROUP NAME ---------> ", self.pat_grp_id)

            elif user.user_type == 'DOCTOR':
                # to check which patient is online
                for self.doc_pat_grp_id in await self._get_user_grp_id(user):
                    # print("Doc connected --------->", self.doc_pat_grp_id)
                    await self.channel_layer.group_add(
                        group=self.doc_pat_grp_id,
                        channel=self.channel_name
                    )
                print(
                    f"THE CHANNEL NAME for doctor ---------> {self.channel_name}")
                print("DOCTOR GROUP NAME --------->", self.doc_pat_grp_id)
            elif user.is_superuser:
                """I will keep the grp_id constant in this case
                shikamaru's the patient and his grp_id = "ed63d330-9b7d-403e-8942-cb6374df4bd1"
                """
                grp_id = "ed63d330-9b7d-403e-8942-cb6374df4bd1"
                await self.channel_layer.group_add(
                    group=f"{grp_id}",
                    channel=self.channel_name
                )
                print(f"HEY LO {user}")
                print(f"Hospital also connected {grp_id}")

            await self.accept()

    """[asynchronous method of sending the data]
    This is a new methodology of implementing the same concept
    """

    # ++++++++++++++++++++++++++++++++++ NEW IMPLEMENTATION ++++++++++++++++++++++++++++++++++
    # the below code is important
    async def broadcast_start_sepsis_data(self, data):
        """This broadcast function will only be allowed to the superuser(ie Hospital)"""
        grp_id = "ed63d330-9b7d-403e-8942-cb6374df4bd1"
        await self.serializer_checking_saving_data(data)
        await self.channel_layer.group_send(
            group=grp_id,
            message={
                'type': 'echo.message',
                'data': data
            }
        )

    #----------------------------------------------------------------#
    """[The code after this is same for both implementation]
    """
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
        print(f"THE SELF {self.channel_name} {self.scope['user']}")
        print(f"THE MESSAGE {message}")
        await self.send_json(message.get('data'))

    async def receive_json(self, content, **kwargs):
        """[summary]
        • All the events received to the server will be evaluated here.
        • If websocket has event-type based on these the receive function will execute
            the respective function
        """
        print("THE RECEIVE FUNCTION RAN")
        message_type = content.get('type')
        print("THE MESSAGE TYPE", message_type)
        if message_type == 'echo.message':
            await self.echo_message(content)

        if message_type == 'broadcast.start_sepsis_data':
            print("THE EVENT BROADCAST=====================")
            await self.broadcast_start_sepsis_data(content.get('data'))
