from dataBase.getConnection import getConn

from midlewares.generateCode import generateCode
from midlewares.generateQRcode import generate_QR_code

def reduceLink(longLink):
    code = generateCode()
    conn = getConn()
    curs = conn.cursor()
    try:
        curs.execute("INSERT INTO links (long_link, code) VALUES (%s, %s)", (longLink, code))
        conn.commit()
        generate_QR_code(code)
        return code
    except Exception as ex:
        return f"Bad! error:{ex}"
    finally:
        conn.close()
        curs.close()