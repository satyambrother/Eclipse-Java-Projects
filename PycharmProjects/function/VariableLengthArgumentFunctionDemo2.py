def sum(name,*n):
    result=0
    for x in n:
        result=result+x
    print("the sum is done by {} and sum is {}: ".format(name,result))
sum('satyam')
sum('deepak1',0,20)
sum('shubham',10,20,30)
sum('harshit',10,20,30,40)


