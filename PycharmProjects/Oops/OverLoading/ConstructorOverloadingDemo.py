# constructor overloading is not required in python

class Test:
    def __init__(self,*a):
        print('constructor of any number of argument')
t=Test(10,20)
t=Test(10,20,30)
t=Test()