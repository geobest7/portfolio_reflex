from pydantic import BaseModel, EmailStr
from typing import Optional

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    is_admin: bool
    
    class Config:
        from_attributes = True

class ChangePassword(BaseModel):
    """Schema para cambiar contraseña"""
    current_password: str
    new_password: str

class ChangeUsername(BaseModel):
    """Schema para cambiar nombre de usuario"""
    new_username: str
    password: str  # Requerir contraseña para confirmar