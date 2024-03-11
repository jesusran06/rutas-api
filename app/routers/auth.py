from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.User import User
from app.services.user import createUserService
from app.config.database import get_db
from app.utils.Security import hash
from sqlalchemy.orm import Session
from app.config.auth import create_token, authenticated_user

auth = APIRouter()

oauth2_scheme = OAuth2PasswordBearer("/token")

@auth.get("/users/me")
def user(token: str = Depends(oauth2_scheme)):
    return "soy user"

@auth.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticated_user(form_data.username, form_data.password, db)
    access_token_jwt = create_token({"sub": user.email})
    return {"access_token": access_token_jwt, "rol":user.rol_id,"token_type": "bearer", "id": user.id}

@auth.get("/")
async def root():
    return {"access_token": "Hello World"}

@auth.post("/user")
async def createUser(user : User, db: Session = Depends(get_db)):
    print(user)
    hashed_password = hash(user.password)
    res = createUserService(db, user, hashed_password)
    print(res)