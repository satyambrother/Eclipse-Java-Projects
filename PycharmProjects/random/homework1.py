n=int(input("enter number of element in list: "))
list=[]
for i in range(n):
    ele = int(input("enter element in list"))
    list.append(ele)
print(list)
for i in range(n):
    j=0
    while j<n:
     if list[j]<0:
        temp=list[j]
        list.remove(list[j])
        list.append(temp)
     j+=1
print(list)

