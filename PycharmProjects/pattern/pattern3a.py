n=int(input('enter no of row:  '))
d='*'
for r in range(1,n+1):

    for s in range(r,n):
        print(" ",end=" ")
    p=(r*2)-1
    for c in range(0,p):
           print(d,end=' ')
    print()