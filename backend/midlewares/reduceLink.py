from backend.dataBase.getConnection import getConn

from backend.midlewares.generateCode import generateCode

def reduceLink(longLink):
    code = generateCode()
    conn = getConn()
    curs = conn.cursor()
    try:
        curs.execute("INSERT INTO links (long_link, code) VALUES (%s, %s)", (longLink, code))
        conn.commit()
        return code
    except Exception as ex:
        return f"Bad! ex:{ex}"
    finally:
        conn.close()
        curs.close()