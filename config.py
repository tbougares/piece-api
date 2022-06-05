from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = "postgresql://postgres:0000@localhost:5432/Piece_de_tache"

engine = create_engine(DATABASE_URL)
sessionLocale = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
