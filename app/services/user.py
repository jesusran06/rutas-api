from app.models.User import User as UserModel
from app.models.Rol import  Rol as RolModel
from sqlalchemy.orm import Session
from app.schemas.User import User, UserActUbi
from fastapi import HTTPException, status

def createUserService(db: Session, user: User, hashed_password: str):
    already_exists = db.query(UserModel).filter(UserModel.email == user.email).first()
    print(user)
    if already_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "User already exists!")
    db_user = UserModel(email=user.email, hashed_password=hashed_password, disabled=user.disabled, rol_id=user.rol,
            full_name=user.full_name, active=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def getUserService(db: Session, email: str):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user:
        return user
    
def updateUbication(db: Session, user: UserActUbi, id: int):
    userDb = db.query(UserModel).filter(UserModel.id == id).first()
    userDb.last_latitude = user.last_latitude
    userDb.last_longitude =  user.last_longitude
    db.commit()
    db.refresh(userDb)
    
def getUserLocations(db: Session, rol: int):
    if rol == 1:
        print('if')
        locations = db.query(UserModel).filter(UserModel.active == True, UserModel.rol_id == 2).all()
    else:
        print('else')
        locations = db.query(UserModel).filter(UserModel.active == True, UserModel.rol_id == 1).all()
        print(locations)
    if locations is None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "Not users active")
    serialized_locations = [
        {"id": location.id, "latitude": location.last_latitude, "longitude": location.last_longitude}
        for location in locations
    ]
    return serialized_locations