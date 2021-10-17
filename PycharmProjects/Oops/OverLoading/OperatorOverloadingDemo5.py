class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self,others):
        return self.salary*others.days
class TimeSheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

    def __mul__(self,others):
        return self.days*others.salary

e=Employee('satyam',500)
t=TimeSheet('satyam',25)

print('This month salary:',e*t)
print('This month salary:',t*e)