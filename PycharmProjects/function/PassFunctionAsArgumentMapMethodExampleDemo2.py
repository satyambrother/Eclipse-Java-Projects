'''l=[1,2,3,4,5]
l1=list(map(lambda a:a*2,l))
print("New modifed list is",l1)'''

# we can also take multiple sequence in map method but ensure that length of second sequence not greater than first sequence

l1=[1,2,3,4,5]
l2=[10,20,30,40]
l=list(map(lambda a,b:a*b,l1,l2))
print("New modifed list is",l)