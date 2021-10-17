import cx_Oracle

try:
    query='create table emp(eno number,ename varchar(20),esal number(10,2),eaddress varchar(10))'
    connection=cx_Oracle.connect('system/satyam1998@localhost')
    cursor=connection.cursor()
    cursor.execute(query)
    print('table created successfully')

except cx_Oracle.DatabaseError as e:
    if connection:
        connection.rollback()
        print('there is a problem',e)
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()