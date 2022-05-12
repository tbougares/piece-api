from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class PieceBase(BaseModel):
    id: int
    nom_piece: str
    prix_piece: float


class RequestPiece(BaseModel):
    nom_piece: str
    prix_piece: float


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
