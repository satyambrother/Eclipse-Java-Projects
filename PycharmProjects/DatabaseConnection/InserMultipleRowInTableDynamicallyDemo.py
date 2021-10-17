import cx_Oracle
try:
    con == cx_Oracle.connect('system/satyam1998@localhost')
    cursor = con.cursor()
    while True:
      eno=int(input('enter employee number'))
      ename=input('enter employee name')
      esal=input('enter employee salary')
      eadd=input('enter employee address')
      query='insert into emp values(%d,'%S',%f,'%S')
      cursor.execute(query,%(eno,ename,esal,eadd))
      con.commit()
      print('record inserted successfully')
      option=input('do you want to insert more record[yes/no]')
      if option=='no:'
                break
except cx_Oracle.DatabaseError as e:

    if con:
        con.rollback()
        print('there is a problem',e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close

