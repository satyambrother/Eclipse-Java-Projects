n=int(input("enter number of element in list: "))

list=[]
for i in range(n):
    ele = int(input("enter element in list"))
    list.append(ele)
print(list)


search=int(input("enter  element which you want to search in list: "))

list.sort()
print(list)
f=0
l=n-1
m=(f+l)//2
while f<=l:
    m=(f+l)//2
    if list[m]==search:
        print("%d item present at location %d"%(search,m+1))
        break
    elif list[m]<search:
        f=m+1

    else:
        l=m-1

if f>l:
  print("search item %d not present in list"%(search))

