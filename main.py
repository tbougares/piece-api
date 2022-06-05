from fastapi import FastAPI
import uvicorn
import Modele
import authentification
import rooterUser
from config import engine
import rooter
import rooterUser
import authentification

Modele.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authentification.router, tags=["Authentification"])
app.include_router(rooter.router, prefix="/piece", tags=["Piece"])
app.include_router(rooterUser.user_router, prefix="/User", tags=["User"])


@app.get("/name")
def show():
    return {"msg": "taher"}


@app.get("/")
def root():
    return {"hello": "world!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080)
