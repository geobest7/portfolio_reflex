"""
Script para crear el primer usuario administrador
Ejecutar: python create_admin.py
"""
from app.database import SessionLocal, engine, Base
from app.models.user import User
from app.utils.auth import get_password_hash

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

def create_admin():
    db = SessionLocal()
    
    try:
        # Verificar si ya existe un admin
        existing_admin = db.query(User).filter(User.username == "admin").first()
        
        if existing_admin:
            print("❌ El usuario 'admin' ya existe")
            return
        
        # Crear usuario admin
        admin_user = User(
            username="admin",
            email="admin@portfolio.com",
            hashed_password=get_password_hash("admin123"),  # Cambiar en producción
            is_active=True,
            is_admin=True
        )
        
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        
        print("✅ Usuario administrador creado exitosamente")
        print(f"   Username: admin")
        print(f"   Password: admin123")
        print(f"   Email: admin@portfolio.com")
        print("\n⚠️  IMPORTANTE: Cambia la contraseña después del primer login")
        
    except Exception as e:
        print(f"❌ Error al crear usuario admin: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_admin()