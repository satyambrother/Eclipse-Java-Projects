class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
         print('My name is   :',self.name)
         print('My roll no is:',self.rollno) # accessing instance variable by using self inside class
s1=Student('satyam',30)
s1.display()
print(s1.name,s1.rollno) # access instance variable outside the class by using reference
print()
s2=Student('deepak',10)
s2.display()
print(s2.name,s2.rollno)
