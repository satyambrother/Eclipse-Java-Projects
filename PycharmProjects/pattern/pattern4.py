n=int(input('enter no of row:  '))

for r in range(1,n+1):
    d=r
    for c in range(r,n+1):
        print(d,end=' ')
        d+=1
    print()
