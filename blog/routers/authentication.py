from fastapi import APIRouter, Depends, Response, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from .. import schemas, models, JWToken
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from datetime import datetime, timedelta, timezone

router = APIRouter(tags=["authentication"])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=404, detail=f"Invalid Password")
    
    access_token_expires = timedelta(minutes=JWToken.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWToken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

