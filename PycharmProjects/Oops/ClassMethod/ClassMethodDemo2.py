class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def getNoOfObject(cls):
        print('number of object created',cls.count)

t1=Test()
t2=Test()
t3=Test()
Test.getNoOfObject()
