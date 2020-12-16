from config import SQL_ENGINE
from models import *

print("Creating Database")
Base.metadata.create_all(SQL_ENGINE)
