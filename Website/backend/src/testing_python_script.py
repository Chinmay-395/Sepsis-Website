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
        'type': 'start.sepsis',
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


async def receive_data_from_start_sepsis():
    ws_pat = websocket.WebSocket()
    ws_pat.connect(
        'ws://localhost:8000/sepsisDynamic/?token=1fe10f828b00e170b3a9c5d41fc168a31facefc3')
    time.sleep(3)
    await initialize_the_sepsis(ws_pat)
    # time.sleep(2)
    while True:
        print("I RAN")
        greeting = await receive_sepsis(ws_pat)
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(receive_data_from_start_sepsis())
