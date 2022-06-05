from datetime import datetime
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field, EmailStr
from pydantic.generics import GenericModel


T = TypeVar('T')


class PieceBase(BaseModel):
    id: int
    nom_piece: str
    prix_piece: float



    class config:
        orm_mode = True





class RequestPiece(BaseModel):
    # parameter: PieceBase = Field(...)

    nom_piece: str
    prix_piece: float


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
#user

class RequestUser(BaseModel):

       username: str
       password: str
       email: str


class ShowUser(BaseModel):
    username: str
    password: str
    email: str
class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str]