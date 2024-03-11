import asyncio
import json
from websockets import connect

class Location:
    async def getCurrentLocation(self):
        async with connect("ws://192.168.0.85:8000/ws/1") as websocket:
            await websocket.send(json.dumps({"type": "location_update"}))
            response = await websocket.recv()
            return json.loads(response)