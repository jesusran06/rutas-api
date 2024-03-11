from app.models.Route import Route as RouteModel
from app.models.Coordenate import Coordenate as CoordenateModel
from sqlalchemy.orm import Session
from app.schemas.Route import RouteFront
from app.schemas.Coordenate import Coordenate
from fastapi import HTTPException, status

def createRouteService(db: Session, route: RouteFront):
    # Paso 1: Crea la Ruta
    db_route = RouteModel(name=route.name, user_id=route.user_id)
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    createCoordenatesService(db, route.coordenates, db_route.id)
    return db_route.id

def createCoordenatesService(db: Session, coordenate: Coordenate, id: int):
    for coord_data in coordenate:
        print(coord_data)
        db_coord = CoordenateModel(latitude= coord_data.latitude, longitude = coord_data.longitude, order = coord_data.order, route_id=id)
        db.add(db_coord)
        
    db.commit()
    db.refresh(db_coord)