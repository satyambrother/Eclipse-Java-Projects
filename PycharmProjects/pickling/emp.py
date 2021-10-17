
class Employee:
    def __init__(self,eno,ename,esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eadd)