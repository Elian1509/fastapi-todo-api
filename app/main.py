from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas, crud
from app.database import engine, get_db
from app.schemas import PriorityEnum

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TODO API",
    description="API para gestión de tareas",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a TODO API",
        "status": "running",
        "version": "1.0.0"
    }

# CREAR tarea
@app.post("/tasks/", response_model=schemas.TaskResponse, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

# LISTAR todas las tareas
@app.get("/tasks/", response_model=List[schemas.TaskResponse])
def read_tasks(priority: Optional[PriorityEnum] = None, category_id: Optional[int] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, priority=priority, category_id=category_id, skip=skip, limit=limit)
    return tasks

# OBTENER una tarea por ID
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

# ACTUALIZAR tarea
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.update_task(db, task_id=task_id, task_update=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

# ELIMINAR tarea
@app.delete("/tasks/{task_id}", response_model=schemas.TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.delete_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task


#######
## Categorias
#######

# CREAR categoria
@app.post("/category/", response_model=schemas.CategoryResponse, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

# LISTAR todas las categorias
@app.get("/category/", response_model=List[schemas.CategoryResponse])
def read_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorys = crud.get_categorys(db, skip=skip, limit=limit)
    return categorys

# OBTENER una categoria por ID
@app.get("/category/{category_id}", response_model=schemas.CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_category

# ACTUALIZAR categoria
@app.put("/category/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db, category_id=category_id, category_update=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_category

# ELIMINAR categoria
@app.delete("/category/{category_id}", response_model=schemas.CategoryResponse)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.delete_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_category