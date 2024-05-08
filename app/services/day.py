from app.models.Day import Day as DayModel
from sqlalchemy.orm import Session
from app.schemas.Day import DayCreate

async def createDaysFirstTime(db: Session):
    already_exists = db.query(DayModel).first()
    if already_exists:
        return
    days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    for day in days:
        db_day = DayModel(name=day)
        db.add(db_day)
        db.commit()
        db.refresh(db_day)