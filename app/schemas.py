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

# Schema para actualizar una tarea
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[PriorityEnum] = None 

# Schema para respuesta (lo que devuelve la API)
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: PriorityEnum
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
