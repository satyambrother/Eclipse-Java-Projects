import cx_Oracle
try:
    con == cx_Oracle.connect('system/satyam1998@localhost')
    cursor = con.cursor()
    cuttoff=float(input('enter cuttoff salary'))
    query='delete from emp where esala>%f'
    cursor.execute(query,%cuttoff)
    con.commit()
    print('record deleted successfully')