n=int(input(" enter number  "))
m=n
l=0
while n>0:
    n=n//10
    l+=1

while l>0:
    p=10**(l-1)
    q=m//p
    m=m%p
    l-=1

    if q == 0:
        print("0")

    elif q == 1:
        print("1")
    elif q == 2:
        print("2")
    elif q == 3:
        print("3")
        # elif q==4:
       # four()
    elif q == 4:
        print("4")
    elif q == 5:
        print("5")
    elif q == 6:
        print("6")
    elif q == 7:
        print("7")
    elif q == 8:
        print("8")
    elif q== 9:
        print("9")
    print("\n")
