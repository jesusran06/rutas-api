from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.User import UserBase
from app.services.user import createUserService
from app.config.database import get_db
from app.utils.Security import hash
from sqlalchemy.orm import Session
from app.config.auth import create_token, authenticated_user
from app.services.configuration import getConfig
from app.services.schedule import getScheduleById

auth = APIRouter()

oauth2_scheme = OAuth2PasswordBearer("/token")

@auth.get("/users/me")
def user(token: str = Depends(oauth2_scheme)):
    return "soy user"

@auth.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = await authenticated_user(form_data.username, form_data.password, db)
    config  = await getConfig(db)
    access_token_jwt = create_token({"sub": user.ci})
    if not config:
        return {"access_token": access_token_jwt, "user":user, "token_type": "bearer", "config": None, "schedule": None}
    else:
      schedule = await getScheduleById(db, config.schedule_id)
      return {"access_token": access_token_jwt, "user":user, "token_type": "bearer", "config": config, "schedule": schedule}

@auth.get("/")
async def root():
    return {"access_token": "Hello World"}

