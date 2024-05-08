from app.schemas.User import UserCreate
from app.config.database import SessionLocal
from app.utils.Security import hash
from app.services.rol import createRolService
from app.services.user import createUserService
from app.schemas.Rol import RolCreate
from app.services.day import createDaysFirstTime

async def init_db():
    db = SessionLocal()
    try:
        rol = RolCreate(name="admin")
        db_rol = await createRolService(db, rol)
        hashed_password = hash("1234")
        user = UserCreate(ci=1, ci_type="v", name="jesus", last_name="rangel", active=True, rol_id=db_rol.id, phone=11, dateBird="1994-01-13",
                          created_at="2024-05-02", updated_at="2024-05-02", password="1234")
        await createUserService(db, user, hashed_password)
        await createDaysFirstTime(db)
        print("Datos por defecto insertados correctamente")
    except Exception as e:
        print(f"Error al insertar datos por defecto: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()