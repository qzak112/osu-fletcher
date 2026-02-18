import asyncio
import websockets
import json
import subprocess

AUDIO_PATH = "/home/arch/fletcher_loud.wav"
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
                max_combo = data["play"]["combo"]["max"]
                
                # Combo break: was above 0, now reset, and max combo was higher
                if last_combo > 10 and current_combo < last_combo and current_combo == 0:
                    print("COMBO BREAK - Fletcher activated")
                    subprocess.Popen(["paplay", AUDIO_PATH])
                
                last_combo = current_combo
            except KeyError:
                pass

asyncio.run(watch_osu())
