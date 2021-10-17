n=int(input("enter number which you want to print : "))
d="*"
for i in range(1,13):
     if i<3 or i>10 or i==6 or i==7:
         for j in range(1,11):
              print(d,end=" ")
     else:
         for j in range(1, 11):
            if j>8 or j<3:
                print(d, end=" ")
            else:
              print(" ", end=" ")
     print()
