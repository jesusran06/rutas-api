from app.models.User import User as UserModel
from sqlalchemy.orm import Session
from app.schemas.User import User
from fastapi import HTTPException, status

async def createUserService(db: Session, user: User, hashed_password: str):
    already_exists = db.query(UserModel).filter(UserModel.ci == user.ci).first()
    
    if already_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= "User already exists!")
    db_user = UserModel(ci=user.ci, hashed_password=hashed_password, ci_type=user.ci_type, rol_id=user.rol_id, name=user.name,
            last_name=user.last_name, phone=user.phone, active=True, date = user.dateBird, created_at=user.created_at, updated_at=user.updated_at)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def getUserService(db: Session, ci: str):
    user = db.query(UserModel).filter(UserModel.ci == ci).first()
    if user:
        return user
    
def getAllUsersService(db: Session):
    users = db.query(UserModel).all()
    return users