class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def info(self):
        self.marks=60
s1=Student('satyam',30)
s1.info()
s1.age=20
print(s1.__dict__)
print()

s2=Student('deepak',9)
s2.info()
s2.age=20
print(s2.__dict__)
