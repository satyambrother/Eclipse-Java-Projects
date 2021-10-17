class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi:',self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print('first division')
        elif self.marks>=50:
            print('second division')
        elif self.marks>=35:
            print('third division')
        else:
            print('you are fail')
n=int(input('enter number of student'))
for i in range(0,n):
    name=input('enter name:')
    marks=int(input('enter subject marks: '))
    s=Student(name,marks)
    s.display()
    s.grade()
    print('*'*20)