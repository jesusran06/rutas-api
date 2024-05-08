from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.schemas.User import UserBase, UserCreate, User
from app.services.user import createUserService, getAllUsersService
from app.config.database import get_db
from app.utils.Security import hash
from sqlalchemy.orm import Session
from fastapi import HTTPException

user = APIRouter()
oauth2_scheme = OAuth2PasswordBearer("/token")
@user.post("/user")
async def createUser(user : UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash(user.password)
    try:
      res = createUserService(db, user, hashed_password)
      return {"user": res, "status": 200}
    except:
      raise HTTPException(status_code=500, detail="Error al crear usuario")
    

@user.get("/usersAll", dependencies=[Depends(oauth2_scheme)])
async def getAllUsers(db: Session = Depends(get_db)):
    try:
      res = getAllUsersService(db)
      return res
    except:
      raise HTTPException(status_code=500, detail="Error al obtener usuarios")
    
    