import csv
with open('student.csv','w',newline="") as f:
    w=csv.writer(f)
    w.writerow(['NAME','ROLLNO','MARKS','ADDRESS'])
    while True:

        name=input('enter student name: ')
        rollno=input('enter student roll number: ')
        marks=input('enter student marks: ')
        address=input('enter student address')
        w.writerow([name,rollno,marks,address])
        option=input('do you want to insert more record [yes/no]')
        if option.lower()=='no':
            break
print('total student data inserted in csv file successfully')