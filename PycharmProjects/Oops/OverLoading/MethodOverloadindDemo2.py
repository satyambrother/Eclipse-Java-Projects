'''1==>Python would not support method overloadind/constructor overloading because
       in method overloading required to declare data type compulsory but in bython
       we are not able to declare data type

   2==>In python method overloading is not required because we can pass anything for
        a single method and get facility of method overloading '''



class Test:
    def m(self,i):
        print(i)
t=Test()
t.m('satyam')
t.m(10)
t.m(10.5)
t.m(10+20j)