def smartdivision(func):
    def inner(a,b):
        if b==0:
           print(' hello stupid... how we can divide with zero ')

        else:
            return func(a,b)
    return inner

@smartdivision
def division(a,b):
    return a/b
print(division(2,3))
print(division(10,3))
print(division(10,0))