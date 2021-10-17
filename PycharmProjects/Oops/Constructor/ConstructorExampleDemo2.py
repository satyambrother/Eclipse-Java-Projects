class Employee:
    '''This class is develop by satyam'''
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def info(self):
        print('*'*20)
        print('Employee Id number is:',self.eno)
        print('Employee name is     :',self.ename)
        print('Employee salary is   :',self.esal)
        print('*'*20)
e1=Employee(101,'satyam',100000)
e1.info()
print()
e2=Employee(102,'deepak',100000)
e2.info()