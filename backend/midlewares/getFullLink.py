from backend.dataBase.getConnection import getConn

def getFullLinkByCode(code):
    conn = getConn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT long_link FROM links WHERE code = %s", (code,))
        data = curs.fetchone()
        return data[0]
    except Exception as ex:
        return f"Bad! ex:{ex}"
    finally:
        conn.close()
        curs.close()