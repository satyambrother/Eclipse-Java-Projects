class Student:
    ''' this class is written by satyam '''
    def __init__(self):
        self.name='satyam'
        self.age=20
        self.marks=80

    def talk(self):
        print('Hello my name is :',self.name)
        print('I am {} year old'.format(self.age))
        print('My marks is:',self.marks)
print(Student.__doc__)
print()
s=Student()
s.talk()


