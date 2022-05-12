from fastapi import APIRouter, HTTPException, Depends
from config import sessionLocale
from sqlalchemy.orm import session
from Schema import PieceBase, RequestPiece, Response
import crud
import Modele

router = APIRouter()


def get_db():
    db = sessionLocale()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_by_id(db: session = Depends(get_db)):
    _Piece = crud.get_Piece(db)
    if _Piece is None:
        raise HTTPException(status_code=404, detail=" not found")
    return _Piece


@router.post("/insert")
async def update_Piece(request: RequestPiece, db: session = Depends(get_db)):
    _Piece = crud.create_Piece(db, request)
    return Response(code=200, status="ok", message="Success update data", result=_Piece)


@router.delete("/{id}")
async def delete(id1: int, db: session = Depends(get_db)):
    crud.remove_Piece(db, id == id1)
    return Response(code=200, status="ok", message="Success delete data", exclude_none=True)
