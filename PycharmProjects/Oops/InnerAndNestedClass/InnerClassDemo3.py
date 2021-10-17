class Person:
    def __init__(self,name,dd,mm,yy):
        self.name=name
        self.dob=self.DOB(dd,mm,yy)  # create inner class object reference
    def display(self):
        print('name:',self.name)
        self.dob.display()           # call inner class display method by using reference

    class DOB:
        def __init__(self,dd,mm,yy):
            self.dd=dd
            self.mm=mm
            self.yy=yy

        def display(self):
            print('DOB:{}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person('deepak',10,9,1998)
p.display()
p.dob.display()