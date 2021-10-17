n=int(input("enter number of element in list: "))
search=int(input("enter  element which you want to search in list: "))
list=[]
for i in range(n):
    ele = int(input("enter element in list"))
    list.append(ele)
print(list)

for j in range(n):
    if list[j]==search:
        print("%d item present at location %d"%(search,j))
    else:
        j+=1
if j==n:
    print("item not present in list")
