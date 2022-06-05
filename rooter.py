from fastapi import APIRouter, HTTPException, Depends

import Schema

from config import sessionLocale
from sqlalchemy.orm import session
from sqlalchemy import delete
from Schema import PieceBase, RequestPiece, Response
import crud
import Modele

import oauth2
#router = APIRouter(dependencies=[Depends(auth_handler.auth_wrapper)])
router=APIRouter()

def get_db():
    db = sessionLocale()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def getAll(db: session = Depends(get_db), current_user :Schema.RequestUser = Depends(oauth2.get_current_user)):
    _Piece = crud.get_Piece(db)
    if _Piece is None:
        raise HTTPException(status_code=404, detail=" not found")
    return _Piece


@router.post("/insert")
async def creat(request: RequestPiece, db: session = Depends(get_db)):
    # _Piece = Modele.Piece_de_tache()
    # _Piece.nom_piece = request.parameter.nom_piece
    # _Piece.prix_piece = request.parameter.prix_piece
    # db.add(_Piece)
    # db.commit()
    # return request
    _Piece = crud.create_Piece(db, request)
    return Response(code=200, status="ok", message="Success Insert Piece avec success", result=_Piece)





@router.put('/{id}')
async def update_Piece(id: int, request: RequestPiece, db: session = Depends(get_db)):
    # _Piece =
    _Piece = crud.Update_Piece(db=db,  nom=request.nom_piece, id_Piece=id, prix=request.prix_piece)
    return Response(code=200, status="ok", message="Success update Piece avec success", result=_Piece)


@router.delete("/{id}")
async def delete(id1: int, db: session = Depends(get_db)):
    crud.remove_Piece(db, Piece_id=id1)
    return Response(code=200, status="ok", message="Success delete data", exclude_none=True)
# _Piece = db.query(Modele.Piece_de_tache).filter(Modele.Piece_de_tache.id_Piece == id1).first()
# if _Piece is None:
#    raise  HTTPException(status_code=404, detail="does existe")


# db.query(Modele.Piece_de_tache).filter(Modele.Piece_de_tache.id_Piece == id1).delete()
# db.comit()
