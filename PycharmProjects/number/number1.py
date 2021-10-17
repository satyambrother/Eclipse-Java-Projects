n=int(input("enter number which you want to print:  "))
d='*'
def zero():
    for i in range(1,3):
        for j in range(1,9):
            print(d,end="")
        print()




def one():
    for i in range(1,9):
        for s in range(1,7):
            print(" ",end=" ")
        for j in range(1,3):
            print(d,end="")
        print()

def two():
    for k in range(1,7):
        print('\n')
    for i in range(1,9):
        for s in range(1,7):
            print(" ",end=" ")
        for j in range(1,3):
            print(d, end="")
        print()


def three():
    for i in range(1,13):
        print('\n')
    for i in range(1,3):
         for j in range(1,9):
             print(d, end="")
         print()

def four():
    for k in range(1,7):
        print('\n')
    for i in range(1,9):
        for j in range(1,3):
            print(d, end="")
        print()

def five():
    for i in range(1,9):
        for j in range(1,3):
            print(d, end="")
        print()
def six():
    for k in range(1,7):
        print('\n')
    for i in range(1,3):
        for j in range(1,9):
            print(d, end="")
        print()
if n==0:
    zero()
    one()
    two()
    three()
    four()
    five()
    six()
elif n==1:
    one()
    two()
elif n==2:

    zero()
    one()
    six()
    four()
    three()
elif n==3:
    zero()
    one()
    two()
    three()
    six()
elif n==4:
    one()
    two()
    five()
    six()
elif n==5:
    zero()
    two()
    three()
    five()
    six()
elif n==6:
    two()
    three()
    four()
    five()
    six()
elif n==7:
    zero()
    one()
    two()
elif n==8:
    zero()
    one()
    two()
    three()
    four()
    five()
    six()
elif n==9:
    zero()
    one()
    two()
    five()
    six()
else:
    print("Invalid. Enter Single digit")













