from fastapi import FastAPI
import uvicorn
import Modele
from config import engine
import rooter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Modele.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(rooter.router, prefix="/piece", tags=["Piece"])


@app.get("/name")
def show():
    return {"msg": "taher"}


@app.get("/")
def root():
    return {"hello": "world!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080)
