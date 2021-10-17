def sum(*n,name):
    result=0
    for x in n:
        result=result+x
    print("the sum is done by {} and sum is {}: ".format(name,result))
sum(name='satyam')
#sum(name='a',10,20) error because positional argument follow keyword argument
sum(10,20,name='deepak')
sum(10,20,30,name='shubham')
sum(10,20,30,40,name='harshit')


