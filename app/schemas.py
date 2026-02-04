from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum 


class PriorityEnum(str, Enum):
    baja = "Baja"
    media = "Media"
    alta = "Alta"

# Schema para crear una tarea
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: PriorityEnum
    category_id: Optional[int] = None

# Schema para actualizar una tarea
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None
    category_id: Optional[int] = None





#######
## Categorias
#######

# Schema para crear una categoria
class CategoryCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Schema para actualizar una categoria
class CategoryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

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
    priority: PriorityEnum
    category_id: Optional[int] = None
    category: Optional[CategoryResponse] = None
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
