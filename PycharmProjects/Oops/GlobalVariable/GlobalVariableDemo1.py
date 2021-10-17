x=100
class Test:
    x=777
    def m1(self):
        x=888
        print(x)
        print(self.x)
    def m2(self):
        print(x)
        print(Test.x)

t=Test()
t.m1()
t.m2()