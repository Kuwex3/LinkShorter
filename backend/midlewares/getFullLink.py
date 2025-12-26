from backend.dataBase.getConnection import getConn

def getFullLinkByCode(code):
    conn = getConn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT long_link FROM links WHERE short_link = %s", (code,))
        data = curs.fetchone()
        print(data[0])
        return data
    except Exception as ex:
        return f"Bad! ex:{ex}"
    finally:
        conn.close()
        curs.close()