d="*"
for i in range(1,13):
    if i<3 or i>10 or i==6 or i==7:
        for j in range(1,12):
            print(d,end=" ")
        print()
    elif i==3 or i==4 or i==5:
        for j in range(1,12):
           if j<3:
               print(d,end=" ")
           else:
            print(" ",end=" ")
        print()
    else:
       for j in range(1,12):
           if j<3 or j==11 or j==10:
              print(d,end=" ")
           else:
               print(" ",end=" ")
       print()


