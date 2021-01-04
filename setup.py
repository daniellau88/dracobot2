from dracobot2.config import SQL_ENGINE
from dracobot2.models import *

print("Creating Database")
Base.metadata.create_all(SQL_ENGINE)
