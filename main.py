from fastapi import FastAPI
from app.routers.auth import auth
from app.routers.route import routeUrl
from app.routers.user import  user
from app.config.database import  Base, engine
import app.models.User
import app.models.Route
import app.models.Coordenate
import app.models.Rol
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "Rutas_app"
app.version = "0.0.1"
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(ErrorHandler)
# app.add_middleware(JWTBearer)
# app.include_router(movie_router)
app.include_router(auth)
app.include_router(routeUrl)
app.include_router(user)
# app.include_router(user_router)

