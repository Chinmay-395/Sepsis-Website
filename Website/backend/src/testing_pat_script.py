import json
import requests
import redis
import websocket
import asyncio
import time
import datetime


async def initialize_the_sepsis(ws_pat):
    for i in range(1, 7):
        ws_pat.send(json.dumps({
            'type': 'broadcast.start_sepsis_data',
            'data': {"YOUNG": "DUMB", }

            # 'type': 'generate.sepsis',
            # 'type': 'start.sepsis',
            # 'data': {
            # "heart_rate": 55,
            # "oxy_saturation": 26.5,
            #     "temperature": 50,
            #     "blood_pressure": 95.48,
            #     "resp_rate": 156,
            #     "mean_art_pre": 85,
            #     "patient": 15
            # # the user_id belongs to shikamaru nara
            # }
        }))
        await asyncio.sleep(10)


async def receive_sepsis(ws_pat):
    return ws_pat.recv()


async def receive_sepses_doc(ws_doc):
    return ws_doc.recv()


async def receive_data_from_start_sepsis():
    # ws_superUser = websocket.WebSocket()
    # ws_superUser.connect(
    #     'ws://localhost:8000/sepsisDynamic/?token=da84a99ccd35761fa91a9a027521cfb5a911e094')
    ws_pat = websocket.WebSocket()
    ws_pat.connect(
        'ws://localhost:8000/sepsisDynamic/?token=c83ab7c31314d2bb9a65029f93530aef34ec2a14')
    # time.sleep(3)
    # ws_doc = websocket.WebSocket()
    # ws_doc.connect(
    #     'ws://localhost:8000/sepsisDynamic/?token=96e1846f6e5b58748cee504f01f2ae7200622fc9')
    # initializing the sepsis generation
    # await initialize_the_sepsis(ws_pat)
    # await asyncio.sleep(3)
    i = 1
    while True:
        print(f"I RAN FOR THE {i}")

        print(f"shika -------> {await receive_sepsis(ws_pat)} \n")
        # print(f"doc ---------> {await receive_sepses_doc(ws_doc)} \n")
        i += 1
        print("\n \n")
        await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(receive_data_from_start_sepsis())
