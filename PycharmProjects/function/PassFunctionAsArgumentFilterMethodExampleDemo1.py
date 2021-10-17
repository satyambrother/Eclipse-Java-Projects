def isEven(a):
    if a%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20]
l1=list(filter(isEven,l))
print(l1)