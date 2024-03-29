from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# NOTE: データベース作成位置
SQLALCHMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SeesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
