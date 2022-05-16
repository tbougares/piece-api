from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('postgres_host')}:5432/Piece_de_tache"

engine = create_engine(DATABASE_URL)
sessionLocale = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
