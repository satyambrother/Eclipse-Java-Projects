n=int(input("enter number of element in list"))
a=[]
for i in range(n):
    a.append(int(input("enter element in list")))
print(a)

for j in range(n):
    min=a[j]
    loc=j
    for k in range(j+1,n):
        if min>a[k]:
            min=a[k]
            loc=k
        temp=a[j]
        a[j]=a[loc]
        a[loc]=temp
        print(a)

print(a)


