from sqlalchemy.orm import session

import Modele
import Schema


def get_Piece(db: session, skip: int = 0, limit: int = 100):
    return db.query(Modele.Piece_de_tache).offset(skip).limit(limit).all()


def get_Piece_code(db: session, Piece_id: int):
    return db.query(Modele.Piece_de_tache).filter(Modele.Piece_de_tache.id_Piece == Piece_id).first()


def create_Piece(db: session, Piece_de_tache: Schema.RequestPiece):
    _Piece = Modele.Piece_de_tache(nom_piece=Piece_de_tache.nom_piece, prix_piece=Piece_de_tache.prix_piece)
    db.add(_Piece)
    db.commit()
    db.refresh(_Piece)
    return _Piece


def remove_Piece(db: session, Piece_id: int):
    _Piece = get_Piece_code(db=db, Piece_id=Piece_id)
    db.delete(_Piece)
    db.commit()
    return _Piece


def Update_Piece(db: session, Piece_id: int, nom: str, prix: float):
    _Piece = get_Piece_code(db=db, Piece_id=Piece_id)
    _Piece.nom_Piece = nom
    _Piece.prix_Piece = prix
    db.commit()
    db.refresh(_Piece)
    return _Piece
