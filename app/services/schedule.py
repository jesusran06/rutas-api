from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from app.models.Schedule import Schedule as ScheduleModel
from app.schemas.Schedule import ScheduleCreate, viewConfigSchedule

async def createSchedule(db: Session, schedule: ScheduleCreate):
    try:
        db_schedule = ScheduleModel(**schedule)
        db.add(db_schedule)
        db.commit()
        db.refresh(db_schedule)
        return db_schedule
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear horario")
    

async def getScheduleById(db: Session, id: int):
    query = text(
            """
            SELECT
                schedule_id,
                schedule_description,
                day_id,
                day_name,
                day_time_init,
                day_time_end,
                state
            FROM
                public."viewConfigSchedule"
            WHERE
                schedule_id = :id
            """
        )
    result = db.execute(query, {"id": id})
    db_schedule = [viewConfigSchedule(**row) for row in result]
    if db_schedule is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")
    else :   
        return db_schedule