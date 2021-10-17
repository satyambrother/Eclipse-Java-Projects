import pickle
class Employee:
    def __init__(self,eno,ename,esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    def display(self):
        print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eadd)
with open('emp.dat','wb')  as f:
    e=Employee(100,'satyam',1000,'ghazipur')
    pickle.dump(e,f)
    print('picklng of employee object successfull')

with open('emp.dat','rb')  as f:
    obj=pickle.load(f)
    print('unpicklng of employee object successfull')
    obj.display()
    print(obj)