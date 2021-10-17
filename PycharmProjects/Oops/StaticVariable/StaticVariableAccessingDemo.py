class Test:
    print('Inside the class \n')
    a=10
    def __init__(self):
        print('Inside constructor')
        print(Test.a)
        print(self.a)

    def m1(self):
        print('Inside instance method')
        print(Test.a)
        print(self.a)

    @classmethod
    def m2(cls):
        print('Inside class method')
        print(Test.a)
        print(cls.a)

    @staticmethod
    def m3():
        print('Inside static method')
        print(Test.a)

t=Test()
t.m1()
t.m2()
t.m3()
print()
print('outside of the class')
print(Test.a)
print(t.a)