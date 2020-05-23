import cx_Oracle


def getDBconnection(username, password):
    ip = 'localhost'
    port = 1521
    SID = 'xe'
    dsn_tns = cx_Oracle.makedsn(ip, port, SID)
    username = 'c##daria'
    password = 'MyPass'

    return cx_Oracle.connect(username, password, dsn_tns, encoding="UTF-8")


def shutDownConnection(con):
    con.close()
    print('Connection closed')


if __name__ == '__main__':
    con = getDBconnection('c##daria', 'MyPass')
    curs = con.cursor()
    curs.execute("select * from masters")
    for row in curs:
        print(row)
