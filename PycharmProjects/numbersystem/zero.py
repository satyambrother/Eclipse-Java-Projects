d="s"
for i in range(1,11):
     if i<3 or i>8:
         for j in range(1,11):
              print(d,end=" ")
     else:
         for j in range(1, 11):
            if j>8 or j<3:
                print(d, end=" ")
            else:
              print(" ", end=" ")
     print()
