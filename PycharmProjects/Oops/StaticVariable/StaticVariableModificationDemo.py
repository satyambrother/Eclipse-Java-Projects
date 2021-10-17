class Test:
    a=10
    def __init__(self):
        Test.a=20
        print('inside constructor value of "a\t":',self.a)
    def m1(self):
        Test.a=30
        print('inside instance method value of "a\t":',self.a)
    @classmethod
    def m2(cls):
        cls.a=40
        print('inside class method value of "a\t":', cls.a)
        Test.a=50
        print('inside class method value of "a\t":', Test.a)
    @staticmethod
    def m3():
        Test.a=60
        print('inside static method value of "a\t":', Test.a)
t=Test()
t.m1()
t.m2()
t.m3()
t.a=70
print(Test.a) #it give the value of static variable inside class
print(t.a)   # it give the value of static variable outside the class after modification
