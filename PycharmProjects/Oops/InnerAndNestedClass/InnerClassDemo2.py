class Person:
    def __init__(self):
        self.name='satyam'
        self.dob=self.DOB()
    def display(self):
        print('name:',self.name)
        self.dob.display()

    class DOB:
        def __init__(self):
            self.dd=9
            self.mm=10
            self.yy=1998

        def display(self):
            print('DOB:{}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person()
p.display()