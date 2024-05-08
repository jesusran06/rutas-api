from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.schemas.Configuration import ConfigurationCreate, ConfigurationUpdate
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.schedule import createSchedule
from app.services.configuration import createConfig, updateConfig
from app.services.daysHours import createDaysHours, updateDaysHours
from fastapi import HTTPException

config = APIRouter()
oauth2_scheme = OAuth2PasswordBearer("/token")
@config.post("/config/createConfig", dependencies=[Depends(oauth2_scheme)])
async def createConfiguration(data : ConfigurationCreate, db: Session = Depends(get_db)):
    scheudule = {
        "description": "config",
    }
    try:
        res_schedule = await createSchedule(db, scheudule)
        config = {
            "exchange_rate" : data.exchange_rate,
            "schedule_id" : res_schedule.id
        }
        res_config = await createConfig(db, config)
        for day in data.days:
            bodyDay = {
                "day_id" : day["id"],
                "schedule_id": res_schedule.id,
                "time_init" : day["start"],
                "time_end" : day["end"]
            }
            await createDaysHours(db, bodyDay)
        return {"config": res_config, "status": 200}
    except:
        raise HTTPException(status_code=500, detail="Error al crear usuario")
    
@config.put("/config/updateConfig", dependencies=[Depends(oauth2_scheme)])
async def updateConfiguration(data: ConfigurationUpdate, db: Session = Depends(get_db)):
    config = {
        "exchange_rate": data.exchange_rate
    }
    try:
        await updateConfig(db, config, data.id)
        for day in data.days:
            bodyDay = {
                "time_init" : day["start"] if day.get("start") else None,
                "time_end" : day["end"] if day.get("end") else None,
                "schedule_id": data.schedule_id,
                "state": day["state"] if day.get("state") else False
            }
            await updateDaysHours(db, bodyDay, day["id"])
        return {"status": 200}
    except:
      raise HTTPException(status_code=500, detail="Error al actualizar configuracion")
    finally:
      db.close()
    
    