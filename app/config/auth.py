from fastapi import HTTPException, Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from app.services.user import getUserService
from app.config.database import get_db
from app.models.User import User as UserModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "Es un secretooo"
ALGORITHM = "HS256"


def create_token(data: dict):
    to_encode = data.copy()
    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return  encoded_token

async def authenticated_user(ci, password, db):
    user = db.query(UserModel).filter(UserModel.ci == ci).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales invalidas", headers={"WWW-Authenticate": "Bearer"})
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas", headers={"WWW-Authenticate": "Bearer"})
    return user


def verify_password(plane_password, hashed_password):
    return pwd_context.verify(plane_password, hashed_password)