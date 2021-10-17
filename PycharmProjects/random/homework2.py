n=int(input("enter number of element in list: "))
list=[]
for i in range(n):
    ele = int(input("enter element in list"))
    list.append(ele)
print(list)
if list[n-1]>=0:
 for i in range(n):
   j=0
   while j<n:
     if list[j]<0:
        temp=list[j]
        list.remove(list[j])
        list.append(temp)
     j+=1
else:
    temp1=list[n-1]
    list.remove(list[n-1])
    for i in range(n-1):
        j=0
        while j<n-1:
            if list[j]<0:
                temp = list[j]
                list.remove(list[j])
                list.append(temp)
            j+=1
    list.append(temp1)

print(list)

