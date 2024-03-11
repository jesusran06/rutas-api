from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.Route import RouteFront
from app.services.route import createRouteService
from app.config.database import get_db
from app.utils.Security import hash
from sqlalchemy.orm import Session
from app.config.auth import create_token, authenticated_user
import json

routeUrl = APIRouter()

oauth2_scheme = OAuth2PasswordBearer("/token")

clients = {}

@routeUrl.get("/Route")
def user(token: str = Depends(oauth2_scheme)):
    return "soy user"

@routeUrl.post("/Route")
async def createRoute(route : RouteFront, db: Session = Depends(get_db)):
    res = createRouteService(db, route)
    print(res)
    
    

        

# @routeUrl.websocket("/ws/updatePositionDriver")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()

#     try:
#         async for data in websocket.iter_text():
#             message = json.loads(data)
#             print(message)
#             user_id = message['id']
#             latitude = message['latitude']
#             longitude = message['longitude']

#             # Almacena la posición actualizada del conductor
#             clients[user_id] = websocket

#             # Retransmite la actualización de posición solo a los clientes interesados
#             await broadcast_position_update(user_id, latitude, longitude, exclude_client=websocket)

#     except WebSocketDisconnect:
#         # Remueve al cliente desconectado de la lista
#         for client_id, client_ws in clients.items():
#             if client_ws == websocket:
#                 del clients[client_id]
#                 break
#         await websocket.close()

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