from fastapi import APIRouter, Depends, Response, status, HTTPException 
from typing import List
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import userRepo

router = APIRouter(prefix="/user", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)    
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepo.create_user(request, db)

@router.get("/{id}", status_code=200)
def show_user(id, db: Session = Depends(get_db)):
    return userRepo.show_user(id, db)
