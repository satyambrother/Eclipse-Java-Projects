# Default argument variable

class Test:

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('sum of three number: ',a+b+c)
        elif a!=None and b!=None:
            print('sum of two number: ',a+b)
        else:
            print('please provide two or three number')

t=Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)
t.sum()