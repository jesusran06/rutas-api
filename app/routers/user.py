from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.User import User, UserActUbi
from app.services.user import createUserService, updateUbication, getUserLocations
from app.config.database import get_db
from app.utils.Security import hash
from sqlalchemy.orm import Session
from app.config.auth import create_token, authenticated_user
import json
from typing import Set
user = APIRouter()

oauth2_scheme = OAuth2PasswordBearer("/token")
active_websockets: Set[WebSocket] = set()
@user.websocket("/ws/updatePositionDriver")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    active_websockets.add(websocket)
    try:
        print('Conexión WebSocket abierta')
        while True:
            data = await websocket.receive_text()
            print('Mensaje recibido:', data)
            data = json.loads(data)
            userUbi = UserActUbi
            userUbi.active = True
            userUbi.last_latitude = data['latitude']
            userUbi.last_longitude = data['longitude']
            updateUbication(db, userUbi, data['id'])
            clients = getUserLocations(db, data['rol'])
            print('clients: ', clients)
            await websocket.send_text(json.dumps(clients))
    except WebSocketDisconnect:
        active_websockets.remove(websocket)
        await websocket.close()
    
    
@user.websocket("/ws/updatePositionClient")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    active_websockets.add(websocket)
    try:
        print('Conexión WebSocket abierta')
        while True:
            data = await websocket.receive_text()
            print('Mensaje recibido:', data)
            data = json.loads(data)
            userUbi = UserActUbi
            userUbi.active = True
            userUbi.last_latitude = data['latitude']
            userUbi.last_longitude = data['longitude']
            updateUbication(db, userUbi, data['id'])
            drivers = getUserLocations(db, data['rol'])
            print('drivers: ', drivers)
            await websocket.send_text(json.dumps(drivers))
    except WebSocketDisconnect:
        active_websockets.remove(websocket)
        await websocket.close()
# async def broadcast_position_update(user_id, latitude, longitude, exclude_client=None):
#     for client_id, client_ws in clients.items():
#         # No envía la actualización al conductor que la envió ni al cliente excluido
#         if client_id != user_id and client_ws != exclude_client:
#             message = {
#                 'type': 'position_update',
#                 'data': {
#                     'userId': user_id,
#                     'latitude': latitude,
#                     'longitude': longitude
#                 },
#             }
#             await client_ws.send_text(json.dumps(message))

