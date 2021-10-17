import cx_Oracle
try:
    query='insert into  emp values(:eno,:ename,:esalary,:eaddress)'
    con==cx_Oracle.connect('system/satyam1998@localhost')
    cursor=con.cursor()
    records=[(100,'a',1000,'gzb'),(200,'b',2000,'gzp')]
    cursor.executemany(query,records)
    con.commit()
    print('record inserted successfully')
except cx_Oracle.Database as e:
    if con:
        con.rollback()
        print('there is a problem')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

