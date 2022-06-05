from datetime import timedelta

from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from passlib.context import CryptContext
import Modele
import Schema
from fastapi import APIRouter, HTTPException, Depends

import tok
from Hashing import Hash

from config import sessionLocale
from sqlalchemy.orm import session



router =APIRouter()

def get_db():
    db = sessionLocale()
    try:
        yield db
    finally:
        db.close()


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: session = Depends(get_db)):
    user = db.query(Modele.User).filter(Modele.User.email == request.username).first()

    if not user:
       raise HTTPException(status_code=404,detail='Invalid Credentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail='Incorrect password')
    access_token = tok.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
