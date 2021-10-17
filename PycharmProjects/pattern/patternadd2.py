n=int(input('enter no of row:  '))
d='*'
q=n*2-1
for r in range(1,q+1):
    if r<n+1:
      for c in range(1,r+1):
           print(d,end=' ')
      print()

    else:
        for j in range(r,q+1):
            print(d, end=' ')
        print()
