import json
import requests
import redis
import websocket
import asyncio
import time
import datetime


async def receive_sepsis(ws_pat):
    return ws_pat.recv()


async def receive_sepses_doc(ws_doc):
    return ws_doc.recv()


async def receive_data_from_start_sepsis():
    # ws_pat = websocket.WebSocket()
    # ws_pat.connect(
    #     'ws://localhost:8000/sepsisDynamic/?token=1fe10f828b00e170b3a9c5d41fc168a31facefc3')
    # time.sleep(3)
    ws_doc = websocket.WebSocket()
    ws_doc.connect(
        'ws://localhost:8000/sepsisDynamic/?token=96e1846f6e5b58748cee504f01f2ae7200622fc9')
    await asyncio.sleep(3)
    # initializing the sepsis generation
    # await initialize_the_sepsis(ws_pat)
    # time.sleep(2)
    i = 1
    while True:
        print(f"I RAN FOR THE {i}")

        # print(f"shika -------> {await receive_sepsis(ws_pat)} \n")
        print(f"doc ---------> {await receive_sepses_doc(ws_doc)} \n")
        i += 1
        print("\n \n")
        await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(receive_data_from_start_sepsis())
