class Outer:
    def __init__(self):
        print('outer class object')
    class Inner:
        def __init__(self):
            print('inner class object')
        def m1(self):
            print('inner class instance method')
    def m2(self):
        print('outer class instance method')
o=Outer()
i=o.Inner()
i.m1()
o.m2()