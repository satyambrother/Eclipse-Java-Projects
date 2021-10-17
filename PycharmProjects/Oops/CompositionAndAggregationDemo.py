class Student:
    collegename='satyam univercity'
    def __init__(self,name):
        self.name=name

print('College name: ',Student.collegename)
s=Student('satyam')
print('Student name:',s.name)

''' without existing student it is not possible to print student name this student name
    and student object relationship is nothing but composition but we print college name 
    with help of class name this relationship is nothing but aggereation'''