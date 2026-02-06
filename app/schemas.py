from pydantic import BaseModel, EmailStr, field_validator, Field
from datetime import datetime
from typing import Optional
from enum import Enum 


class PriorityEnum(str, Enum):
    baja = "Baja"
    media = "Media"
    alta = "Alta"

# Schema para crear una tarea
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Optional[PriorityEnum] = None
    category_id: Optional[int] = None
    
    @field_validator('title')
    def validate_title(cls, v):
        if v and not v.strip():
            raise ValueError('El título no puede estar vacío')
        return v.strip()

# Schema para actualizar una tarea
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None
    category_id: Optional[int] = None
    
    @field_validator('title')
    def validate_title(cls, v):
        if v is not None and not v.strip():
            raise ValueError('El título no puede estar vacío')
        return v.strip() if v else v

## Categorias

# Schema para crear una categoria
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    
    @field_validator('name')
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError('El nombre no puede estar vacío')
        return v.strip()

# Schema para actualizar una categoria
class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    
    @field_validator('name')
    def validate_name(cls, v):
        if v is not None and not v.strip():
            raise ValueError('El nombre no puede estar vacío')
        return v.strip() if v else v

## Usuarios 

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    
    @field_validator('password')
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('La contraseña debe contener al menos un número')
        if not any(char.isalpha() for char in v):
            raise ValueError('La contraseña debe contener al menos una letra')
        return v

## Token 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

## Respuestas Api

# Schema para respuesta (lo que devuelve la API de categorias)
class CategoryResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]

    class Config:
        from_attributes = True

# Schema para respuesta (lo que devuelve la API de tareas)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    priority: PriorityEnum
    category_id: Optional[int] = None
    category: Optional[CategoryResponse] = None
    owner_id: int 
    created_at: datetime
    updated_at: Optional[datetime]
    class Config:
        from_attributes = True
        
# Schema para respuesta (lo que devuelve la API de usuarios)
class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True