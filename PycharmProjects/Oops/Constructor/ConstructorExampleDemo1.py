class Test:
    def __init__(self):
        print('no argument')
    def __init__(self,x):
        print('one argument')
'''t1=Test()
   t2=Test(10)   because method overloading and constructor overloading is not possible in python due to
                 this most recent call constructor is only used in class '''

t2=Test(12)
t2=Test(10)