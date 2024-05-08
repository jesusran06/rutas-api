from sqlalchemy.orm import Session
from app.schemas.Configuration import ConfigurationBase
from fastapi import HTTPException, status
from app.models.DaysHours import DaysHours as DaysHoursModel


async def createDaysHours(db: Session, dayhour: dict):
    try:
        db_config = DaysHoursModel(**dayhour)
        db.add(db_config)
        db.commit()
        db.refresh(db_config)
        return db_config
    except:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la dia y hora")
  
async def updateDaysHours(db: Session, dayhour: dict, id: int):
    try:
        db_dayHour = db.query(DaysHoursModel).filter(DaysHoursModel.schedule_id == dayhour["schedule_id"]).filter(DaysHoursModel.day_id == id).first()
        if db_dayHour is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el dia y hora")
        else:
            db_dayHour.time_init = dayhour["time_init"]
            db_dayHour.time_end = dayhour["time_end"]
            db_dayHour.state = dayhour["state"]
            db.commit()
            db.refresh(db_dayHour)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No se puedo crear el dia y hora")
        