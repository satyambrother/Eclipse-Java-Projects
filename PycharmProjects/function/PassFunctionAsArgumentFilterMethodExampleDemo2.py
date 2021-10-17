l=[0,5,10,15,20]
l1=list(filter(lambda a:a%2!=0,l))
print("list of odd number",l1)

l2=list(filter(lambda a:a%2==0,l))
print("list of even number",l2)