import easyapi
from app.db import sqlite_db

class CompanyDao(easyapi.BusinessBaseDao):
    __tablename__ = 'companys'
    __db__ = sqlite_db
    

class KindDao(easyapi.BusinessBaseDao):
    __tablename__ = 'kinds'
    __db__ = sqlite_db

class ResultDao(easyapi.BusinessBaseDao):
    __tablename__ = 'results'
    __db__ = sqlite_db

