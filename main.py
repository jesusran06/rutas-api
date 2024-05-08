from fastapi import FastAPI
from app.routers.auth import auth
from app.routers.user import  user
from app.initData import init_db
from app.routers.configuration import config
from app.config.database import  Base, engine
import app.models.User
import app.models.Rol
import app.models.Client
import app.models.Card
import app.models.Plan
import app.models.Promotion
import app.models.Suscription
import app.models.Payment
import app.models.PaymentType
import app.models.Day
import app.models.Training
import app.models.DaysHours
import app.models.Schedule
import app.models.EquipExercise
import app.models.Equipment
import app.models.Exercise
import app.models.RouitneExercise
import app.models.Routine
import app.models.HistoryAsist
import app.models.PlanTraining
import app.models.HistoryAction
import app.models.Configuration
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.title = "GYMBRO_APP"
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
app.include_router(user)
app.include_router(config)
# app.include_router(user_router)

async def startup_event():
    await init_db()

# Registrar función de inicio de la aplicación
app.add_event_handler("startup", startup_event)