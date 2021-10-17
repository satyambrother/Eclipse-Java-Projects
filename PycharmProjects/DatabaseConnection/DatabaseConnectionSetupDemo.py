import cx_Oracle
con=cx_Oracle.connect('system/satyam1998@localhost')
if con!=None:
    print('connection establish successfully')
    print('version:',con.version)
else:
    print('connection not establish')
con.close()