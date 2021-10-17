n=int(input("enter number:  "))
def zero():
    d="0"
    for i in range(1, 11):
        if i < 3 or i > 8:
            for j in range(1, 11):
                print(d, end=" ")
        else:
            for j in range(1, 11):
                if j > 8 or j < 3:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
        print()

def one():
    d="1"
    for i in range(1, 11):
        for j in range(1, 3):
            print(d, end=" ")

        print()

def two():
    d="2"
    for i in range(1, 13):
        if i < 3 or i > 10 or i == 6 or i == 7:
            for j in range(1, 12):
                print(d, end=" ")
            print()

        elif i == 3 or i == 4 or i == 5:
            for j in range(1, 12):
                if j < 10:
                    print(" ", end=" ")
                else:
                    print(d, end=" ")
            print()
        else:
            for j in range(1, 3):
                print(d, end=" ")
            print()

def three():
    d="3"
    for i in range(1, 13):
        if i < 3 or i > 10 or i == 6 or i == 7:
            for j in range(1, 12):
                print(d, end=" ")
            print()

        elif i == 3 or i == 4 or i == 5:
            for j in range(1, 12):
                if j < 10:
                    print(" ", end=" ")
                else:
                    print(d, end=" ")
            print()
        else:
            for j in range(1, 12):
                if j < 10:
                    print(" ", end=" ")
                else:
                    print(d, end=" ")
            print()
def four():
    d = "4"
    for i in range(1, 13):
        if i == 7 or i == 8:
            for j in range(1, 12):
                print(d, end=" ")
            print()

        elif i < 7:
            for j in range(1, 12):
                if j < 3 or j > 9:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()
        else:
            for j in range(1, 12):
                if j > 9:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()

def five():
    d = "5"
    for i in range(1, 13):
        if i < 3 or i > 10 or i == 6 or i == 7:
            for j in range(1, 12):
                print(d, end=" ")
            print()
        elif i == 3 or i == 4 or i == 5:
            for j in range(1, 12):
                if j < 3:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()
        else:
            for j in range(1, 12):
                if j < 10:
                    print(" ", end=" ")
                else:
                    print(d, end=" ")
            print()
def six():
    d = "6"
    for i in range(1, 13):
        if i < 3 or i > 10 or i == 6 or i == 7:
            for j in range(1, 12):
                print(d, end=" ")
            print()
        elif i == 3 or i == 4 or i == 5:
            for j in range(1, 12):
                if j < 3:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()
        else:
            for j in range(1, 12):
                if j < 3 or j == 11 or j == 10:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()



def eight():
    d = "8"
    for i in range(1, 13):
        if i < 3 or i > 10 or i == 6 or i == 7:
            for j in range(1, 11):
                print(d, end=" ")
        else:
            for j in range(1, 11):
                if j > 8 or j < 3:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
        print()

def seven():
    d = "7"
    for i in range(1, 11):
        if i < 3:
            for j in range(1, 11):
                print(d, end=" ")
        else:
            for j in range(1, 11):
                if j > 8:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
        print()
def nine():
    d = "9"
    for i in range(1, 13):
        if i < 3 or i > 10 or i == 6 or i == 7:
            for j in range(1, 12):
                print(d, end=" ")
            print()
        elif i == 3 or i == 4 or i == 5:
            for j in range(1, 12):
                if j > 9 or j < 3:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()
        else:
            for j in range(1, 12):
                if j == 11 or j == 10:
                    print(d, end=" ")
                else:
                    print(" ", end=" ")
            print()

while n>0:
    q=n%10
    n=n//10
    if q==0:
        zero()

    elif q==1:
        one()
    elif q==2:
        two()
    elif q==3:
        three()
    #elif q==4:
        four()
    elif q==4:
        four()
    elif q==5:
        five()
    elif q==6:
        six()
    elif q==7:
        seven()
    elif q==8:
        eight()
    else:
        nine()
    print("\n")













