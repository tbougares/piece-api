from sqlalchemy import Column, Integer, String, Float
from config import Base


class Piece_de_tache(Base):
    __tablename__ = "piece"

    id_Piece = Column(Integer, primary_key=True, index=True)
    nom_piece = Column(String, index=True)
    prix_piece = Column(Float)

#USER

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    email = Column(String)