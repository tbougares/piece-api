from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse
from starlette.status import HTTP_201_CREATED

import crud
from Schema import RequestUser, Response
from config import sessionLocale
from sqlalchemy.orm import session


user_router = APIRouter()



def get_db():
    db = sessionLocale()
    try:
        yield db
    finally:
        db.close()


@user_router.post('/User')
async def register(request: RequestUser, db: session = Depends(get_db)):
    _User = crud.create_User(db, request)
    return Response(code=200, status="ok", message="Success Insert User avec success", result=_User)


@user_router.get('/')
async def getAll(db: session = Depends(get_db)):
    _User = crud.get_User(db)
    if _User is None:
        raise HTTPException(status_code=404, detail=" not found")
    return _User
