from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status
from .. import models, schemas
from ..database import get_db
from ..hashing import Hash

def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash().bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} is not available")
    
    return user