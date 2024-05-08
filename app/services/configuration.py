from sqlalchemy.orm import Session
from app.schemas.Configuration import ConfigurationSave, ConfigurationBase
from fastapi import HTTPException, status
from app.models.Configuration import Configuration as ConfigurationModel

async def getConfig(db: Session):
    config = db.query(ConfigurationModel).first()
    if config is None:
        return None
    else:
        return config

async def createConfig (db: Session, config: ConfigurationSave):
    try:
        db_config = ConfigurationModel(**config)
        db.add(db_config)
        db.commit()
        db.refresh(db_config)
        return db_config
    except:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la configuracion")
  
async def updateConfig (db:Session, config: dict, id:int):
    try:
        db_config = db.query(ConfigurationModel).filter(ConfigurationModel.id == id).first()
        if db_config is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuracion no encontrada")
        else:
            db_config.exchange_rate = config["exchange_rate"]
            db.commit()
            db.refresh(db_config)
            return db_config
    except:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear configuracion")
    