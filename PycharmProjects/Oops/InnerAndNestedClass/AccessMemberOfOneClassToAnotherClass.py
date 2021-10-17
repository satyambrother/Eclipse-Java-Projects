class Employee:
    def __init__(self,eno,ename,esalary):
        self.eno=eno
        self.ename=ename
        self.esalary=esalary
    def display(self):
        print('Employee id:     ',self.eno)
        print('Employee name:   ',self.ename)
        print('Employee salary: ',self.esalary)

class Test:
    def modify(emp):                 # it is static method
        emp.esalary=emp.esalary+10000
        emp.display()
e=Employee(30,'satyam',10000)
Test.modify(e)
