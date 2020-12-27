from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()


SQL_ENGINE_URL = 'mysql://%s:%s@localhost/dragon_trainer' % (
    os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'])
SQL_ENGINE = create_engine(SQL_ENGINE_URL, echo=True)

SessionLocal = sessionmaker(bind=SQL_ENGINE, autocommit=False, autoflush=False)
