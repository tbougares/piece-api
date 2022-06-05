from sqlalchemy.orm import session
from passlib.context import CryptContext
import Modele
import Schema


def get_Piece(db: session, skip: int = 0, limit: int = 100):
    return db.query(Modele.Piece_de_tache).offset(skip).limit(limit).all()


def get_Piece_code(db: session, Piece_id: int):
    return db.query(Modele.Piece_de_tache).filter(Modele.Piece_de_tache.id_Piece == Piece_id).first()


def create_Piece(db: session, piece: Schema.RequestPiece):
    _Piece = Modele.Piece_de_tache(nom_piece=piece.nom_piece, prix_piece=piece.prix_piece)
    db.add(_Piece)
    db.commit()
    db.refresh(_Piece)
    return _Piece


def remove_Piece(db: session, Piece_id: int):
    _Piece = get_Piece_code(db=db, Piece_id=Piece_id)
    db.delete(_Piece)
    db.commit()
    return _Piece


def Update_Piece(db: session, id_Piece: int, nom: str, prix: float):

    _Piece = get_Piece_code(db=db, Piece_id=id_Piece)
    _Piece.nom_piece = nom
    _Piece.prix_piece = prix
    db.add(_Piece)
    db.commit()
    return _Piece

#USER
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create_User(db: session, user: Schema.RequestUser):
    hashedPassword= pwd_context.hash(user.password)
    _User = Modele.User(username=user.username, password=hashedPassword, email=user.email)
    db.add(_User)
    db.commit()
    db.refresh(_User)
    return _User

def get_User(db: session, skip: int = 0, limit: int = 100):
    return db.query(Modele.User).offset(skip).limit(limit).all()