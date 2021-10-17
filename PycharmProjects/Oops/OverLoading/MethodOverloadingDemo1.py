# Python not support method overloading but class can have more than one method same name last method consider as useful method

class Test:
    def m1(self):
        print('no argument method')
    def m1(self,x):
        print('one argument method')
t=Test()
#t.m1() it is not consider as method
t.m1(10)
