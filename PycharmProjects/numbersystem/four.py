d="*"
for i in range(1,13):
    if i==7 or i==8:
        for j in range(1,12):
            print(d,end=" ")
        print()

    elif i<7:
        for j in range(1,12):
           if j<3 or j>9:
               print(d,end=" ")
           else:
            print(" ",end=" ")
        print()
    else:
       for j in range(1, 12):
           if j>9:
              print(d,end=" ")
           else:
               print(" ",end=" ")
       print()


