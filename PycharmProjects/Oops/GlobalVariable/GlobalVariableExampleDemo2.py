
class Test:
    def m1(self):
        global x
        x=888
        print(x)

    def m2(self):
        print(x)

t=Test()
t.m1()
t.m2()
print(x)