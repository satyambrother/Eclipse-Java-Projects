import emp,pickle
f=open('emp.dat','wb')
n=int(input('enter number of employee: '))
for i in range(n):
    eno=int(input('enter employee number'))
    ename=input('enter employee name')
    esal=input('enter employee salary')
    eadd=input('enter employee address')
    e=emp.Employee(eno,ename,esal,eadd)
    pickle.dump(e,f)
    print('picklng of employee object successfull')