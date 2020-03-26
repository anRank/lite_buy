import easyapi
from app.config import Config

sqlite_db = easyapi.SqliteDB(database=Config.SQLITE_FILE)

sqlite_db.connect()
