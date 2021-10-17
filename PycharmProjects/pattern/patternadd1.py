n=int(input('enter no of row:  '))
d='*'
for r in range(1,n+1):

    for s in range(1,r):
        print(" ",end=" ")
    p=n+2
    for c in range(1,n+1 ):
           print(d,end=' ')
    print()