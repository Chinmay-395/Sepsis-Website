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
    async def _generate_sudo_sepsis_data(self, data):
        data.update({'heart_rate': random.randint(24, 200)})
        data.update({'oxy_saturation': random.randint(24, 200)})
        data.update({'temperature': random.randint(24, 200)})
        data.update({'blood_pressure': random.randint(24, 200)})
        data.update({'resp_rate': random.randint(24, 200)})
        data.update({'mean_art_pre': random.randint(24, 200)})
        print("-------------", data)
        serializer = SepsisPatientSerializer(data=data)
        print("THE SERIALIZER", serializer)
        return data

    @database_sync_to_async
    def _get_user_grp_id(self, user):
        """This will return grp_id since django channels' channel-layer requires ASCII unicode as group"""
        print("************** THE grp function initiated **************")
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
        print(
            f"THE DATA is {data['patient']} AGAINST USER_ID {self.scope['user'].id}")
        if (str(self.scope['user'].user_type) == 'PATIENT' and self.scope['user'].id == data['patient']):
            x = get_user_model().objects.get(id=data['patient'])
            x = x.patient_set.values('id')[0]['id']
            data.update({'patient': x})
            print("THE DATA AFTER THE USER_ID IS MATCHED WITH THE PATIENT", data)
            return data

    @database_sync_to_async
    def serializer_checking_saving_data(self, data):
        serializer = SepsisPatientSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        x = serializer.create(serializer.validated_data)
        return SepsisPatientSerializer(x).data

    @database_sync_to_async
    def _created_sepsis_data(self, data):
        """This helper function would generate and return the"""
        print(f"THE DATA is {data} AGAINST USER_ID {self.scope['user'].id}")

        """Once the user_id matches with user-id sent 
            through the start_sepsis data we find the 
            patient_id of that user(patient) and generate a
            random values for the patient's sepsis data
        """
        for i in range(10):
            # time.sleep(3)
            data.update({'heart_rate': random.randint(24, 200)})
            data.update({'oxy_saturation': random.randint(24, 200)})
            data.update({'temperature': random.randint(24, 200)})
            data.update({'blood_pressure': random.randint(24, 200)})
            data.update({'resp_rate': random.randint(24, 200)})
            data.update({'mean_art_pre': random.randint(24, 200)})
            # serializing the data
            # print("THE DATA THAT NEEDS TO BE SAVED", data)
            yield data

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
        user = self.scope['user']

        if user.is_anonymous:
            print("user was unknown")
            await self.close()
        else:
            if user.user_type == 'PATIENT':
                self.pat_grp_id = await self._get_user_grp_id(user)
                await self.channel_layer.group_add(
                    group=self.pat_grp_id,
                    channel=self.channel_name
                )
                print("CONNECT TO ---------> ", self.pat_grp_id)

            elif user.user_type == 'DOCTOR':
                # to check which patient is online
                for self.doc_pat_grp_id in await self._get_user_grp_id(user):
                    print("Doc connected --------->", self.doc_pat_grp_id)
                    await self.channel_layer.group_add(
                        group=self.doc_pat_grp_id,
                        channel=self.channel_name
                    )
                print("Doc connected ", self.doc_pat_grp_id)
            await self.accept()

    @database_sync_to_async
    def generate_save_sepsis_data(self, data):
        for i in range(100):
            # time.sleep(1)
            # generate
            pass

    async def start_sepsis(self, message):
        data = message.get('data')
        """ The data we got here was with user_id we need to convert it into patient_id """
        print("THE DATA SENT BY PATIENT INITIALLY ---------------------> ", data)
        get_pat_id_in_data = await self._convert_user_id_to_patient_id(data)
        """we have converted the user_id to patient_id"""
        data = get_pat_id_in_data
        print(f"\n the converted data is ------> {data} \n")
        for generated_and_saved_data in await self._created_sepsis_data(data):
            print("THE DATA THAT NEEDS TO BE SAVED ------->",
                  generated_and_saved_data)
            """Above we generated a new sepsis data that needs to be serialized and saved into database"""
            x = await self.serializer_checking_saving_data(generated_and_saved_data)
            await self.channel_layer.group_send(
                group=self.pat_grp_id,
                message={
                    'type': 'echo.message',
                    'data': x
                }
            )

    """[asynchronous method of sending the data]
    This is a new methodology of implementing the same concept
    """
    async def create_and_save_sepsis_data(self, data):
        pass

    # new sepsis
    async def generating_patient_sepsis(self, message):
        # get the data from message
        data = message.get('data')
        print(f"THE INITIAL DATA {data}")
        # get the patient's id
        get_pat_id_in_data = await self._convert_user_id_to_patient_id(data)
        data = get_pat_id_in_data
        while True:
            time.sleep(5)
            await asyncio.sleep(1)
            # random sepsis data generated and `data` variable is mutated
            data.update({'heart_rate': random.randint(24, 200)})
            data.update({'oxy_saturation': random.randint(24, 200)})
            data.update({'temperature': random.randint(24, 200)})
            data.update({'blood_pressure': random.randint(24, 200)})
            data.update({'resp_rate': random.randint(24, 200)})
            data.update({'mean_art_pre': random.randint(24, 200)})
            print(f"THE DATA  --> {data}")
            # serializing and saving the data
            x = await self.serializer_checking_saving_data(data)
            # send the data to the channel
            await self.channel_layer.group_send(
                group=self.pat_grp_id,
                message={
                    'type': 'echo.message',
                    'data': x
                }
            )

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
            await self.channel_layer.group_send(
                group=self.doc_pat_grp_id,
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
        # this is for new sepsis method
        if message_type == 'generate.sepsis':
            await self.generating_patient_sepsis(content)
        ####################################
        if message_type == 'echo.message':
            await self.send_json({
                'type': message_type,
                'data': content.get('data'),
            })
        if message_type == 'echo.group_message':
            await self.echo_group_message(content)
