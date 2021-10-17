n=int(input("enter number of element in list "))
a=[]
for i in range(n):
    a.append(int(input("enter element in list ")))
print("my unsorted list is{} ".format(a))
for k in range(1,n):
    j=k
    while j>0 and a[j-1]>a[j]:
        temp=a[j]
        a[j]=a[j-1]
        a[j-1]=temp
        j-=1
        print(a)
    print()
print("my sorted list is {} ".format(a))


