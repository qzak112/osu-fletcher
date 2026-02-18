import asyncio
import websockets
import json
import winsound
import os

AUDIO_PATH = os.path.expanduser("~\\fletcher_loud.wav")
last_combo = 0

async def watch_osu():
    global last_combo
    uri = "ws://127.0.0.1:24050/websocket/v2"
    
    async with websockets.connect(uri) as ws:
        print("Connected to tosu, watching for combo breaks...")
        async for message in ws:
            data = json.loads(message)
            
            try:
                current_combo = data["play"]["combo"]["current"]
                
                if last_combo > 10 and current_combo < last_combo and current_combo == 0:
                    print("COMBO BREAK - Fletcher activated")
                    winsound.PlaySound(AUDIO_PATH, winsound.SND_FILENAME | winsound.SND_ASYNC)
                
                last_combo = current_combo
            except KeyError:
                pass

asyncio.run(watch_osu())
