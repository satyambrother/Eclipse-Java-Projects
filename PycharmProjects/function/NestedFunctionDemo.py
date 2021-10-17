
# to fullfill function specific repeatablity we use nested function
'''def f1():
    def f2(a,b):
        print('The sum of {} and {} b is {}'.format(a,b,a+b))
        print('average of given number is',(a+b)/2)
        print()
    f2(10,20)
    f2(100,200)
    f2(1000,2000)
    f2(10000,20000)
f1() '''

# a function can return another function  possible in python

'''def outer():
    print('outer function started')
    def inner():
        print('inner function executed')
    print('outer function returning inner function')
    return inner
f1=outer()
f1()
f1()
f1()
f1()'''

# f1=outer() function call

# f1=outer  for outer function we give another name

def outer():
    print('outer function started')
    def inner():
        print('inner function executed')
    print('outer function returning inner function')
    return inner()
f1=outer()
print(f1)