class Student:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def delete(self):
        del self.a
s1=Student()
s1.delete()
print(s1.__dict__)
print()

s2=Student()
del s2.b
print(s2.__dict__)
