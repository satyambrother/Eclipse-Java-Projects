class Student:

    '''  this class is written by satyam '''
    def __init__(self,name,age,marks):
          self.name=name
          self.age=age
          self.marks=marks

    def talk(self):
        print('Hello my name is :', self.name)
        print('I am {} year old'.format(self.age))
        print('My marks is:', self.marks)

print(Student.__doc__)
print()
s=Student('satyam',23,80)
s.talk()

s=Student('shubam',23,80)
s.talk()