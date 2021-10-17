n=int(input("enter number which you want to print : "))
d="*"
for i in range(1,11):
     if i<3 :
         for j in range(1,11):
              print(d,end=" ")
     else:
         for j in range(1, 11):
            if j>8:
                print(d, end=" ")
            else:
              print(" ", end=" ")
     print()


