import cx_Oracle
try:
    con == cx_Oracle.connect('system/satyam1998@localhost')
    cursor = con.cursor()
    increment=float(input('enter increment salary: '))
    salaryrange=float(input('enter salary range'))
    query='update emp set esalary=esalary+%f where esal<%f'
    cursor.execute(query%(increment,salaryrange))
    con.commit()
    print('record update successfully')
