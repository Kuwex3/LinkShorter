import psycopg2

from backend.dataBase.config import dbname, user, password, host

def getConn():
    connect = psycopg2.connect(dbname = dbname,user =  user, password = password, host = host)
    return connect