class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self,others):
        return self.marks<others.marks
s1=Student('satyam',100)
s2=Student('shivam',200)
print(s1<s2)
print(s2<s1)