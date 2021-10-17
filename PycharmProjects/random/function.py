
# function without parameter and no return type
import os

a = int(input("enter first number i: "))
b = int(input('enter second number: '))


def add(a,b):


    sum=a+b
    print("sum of given number is%d"%(sum))
    return
def sub(a,b):

    diff=a-b
    print("difference of given number is%d" %(diff))
    return
def mul(a,b):

    pro=a*b
    print("product of given number is%d" %(pro))
    return
def div(a,b):

    rat=a/b
    print("ratio  of given number is%1.0f" %(rat))
    return
def menu():
    ans=True
    while ans:
        os.system("cls")
        print("calculater")
        print("1.Add")
        print("2.Substract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        ch = int(input("Enter Choice(1-5):"))
        if ch == 1:
            add(a,b)
        elif ch == 2:
            sub(a,b)
        elif ch == 3:
            mul(a,b)
        elif ch == 4:
            div(a,b)
        elif ch == 5:
            ans = False
        else:
            print("Invalid Choice")
        input("\n\nPress any key......")


if __name__=="__main__":
    menu()
