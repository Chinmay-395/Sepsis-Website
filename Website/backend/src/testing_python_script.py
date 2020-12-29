import json
import requests
import redis
import websocket
import asyncio
import time
import datetime

# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)

# asyncio.run(display_date())
#=============================================================#


async def initialize_the_sepsis(ws_pat):
    ws_pat.send(json.dumps({
        'type': 'generate.sepsis',
        # 'type': 'start.sepsis',
        'data': {
            "heart_rate": 55,
            "oxy_saturation": 26.5,
                "temperature": 50,
                "blood_pressure": 95.48,
                "resp_rate": 156,
                "mean_art_pre": 85,
                "patient": 15  # the user_id belongs to shikamaru nara
        }
    }))


async def receive_sepsis(ws_pat):
    return ws_pat.recv()


async def receive_sepses_doc(ws_doc):
    return ws_doc.recv()


async def receive_data_from_start_sepsis():
    ws_pat = websocket.WebSocket()
    ws_pat.connect(
        'ws://localhost:8000/sepsisDynamic/?token=1fe10f828b00e170b3a9c5d41fc168a31facefc3')
    time.sleep(3)
    # ws_doc = websocket.WebSocket()
    # ws_doc.connect(
    #     'ws://localhost:8000/sepsisDynamic/?token=96e1846f6e5b58748cee504f01f2ae7200622fc9')
    # time.sleep(3)
    # ws_pat_chogi = websocket.WebSocket()
    # ws_pat_chogi.connect(
    #     'ws://localhost:8000/sepsisDynamic/?token=7b5d7f5659f4287dc53821022c2c36c4fe57053c')
    await initialize_the_sepsis(ws_pat)
    # time.sleep(2)
    i = 1
    while True:
        print(f"I RAN FOR THE {i}")

        print(f"shika -------> {await receive_sepsis(ws_pat)} \n")
        # print(f"doc ---------> {await receive_sepses_doc(ws_doc)} \n")
        i += 1
        print("\n \n")
        await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(receive_data_from_start_sepsis())
