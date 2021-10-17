n=int(input("enter number of element in list "))
a=[]
for i in range(n):
    a.append(int(input("enter element in list ")))
print(a)
print()
for k in range(n):
    for j in range(n-k-1):
      if a[j]>a[j+1]:
        temp=a[j]
        a[j]=a[j+1]
        a[j+1]=temp
        print(a)
    print()


