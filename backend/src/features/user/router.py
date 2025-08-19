from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import service, schema
from infra.database import get_db

router = APIRouter()
service = service.UserService()

@router.get("/{id}", response_model=schema.UserRead)
def get_user(id: int, db: Session = Depends(get_db)):
    return service.get_user(db, id)

@router.post("/", response_model=schema.UserRead)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = service.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
    