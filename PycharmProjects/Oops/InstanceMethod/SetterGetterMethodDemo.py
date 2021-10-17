class Student:
    def SetName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def SetMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input('enter number of student: '))
for i in range(n):
    name=input('enter Student name: ')
    marks=int(input('enter subject marks: '))
    s=Student()
    s.SetName(name)
    s.SetMarks(marks)

    print('Hi ',s.getName())
    print('your marks: ', s.getMarks())
    print('*'*20)