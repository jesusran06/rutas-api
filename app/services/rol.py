from app.models.Rol import Rol as RolModel
from sqlalchemy.orm import Session
from app.schemas.Rol import Rol
from fastapi import HTTPException, status

async def createRolService(db: Session, rol: Rol):
    already_exists = db.query(RolModel).filter(RolModel.name == rol.name).first()
    
    if already_exists:
        return
    db_rol = RolModel(name=rol.name)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol