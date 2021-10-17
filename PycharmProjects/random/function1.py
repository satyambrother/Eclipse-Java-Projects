
# function without parameter and no return type
import os
def add():
    a = int(input("enter first number i: "))
    b = int(input('enter second number: '))

    sum=a+b
    print("sum of given number is%d"%(sum))

def sub():
    a = int(input("enter first number i: "))
    b = int(input('enter second number: '))

    diff=a-b
    print("difference of given number is%d" %(diff))

def mul():
    a = int(input("enter first number i: "))
    b = int(input('enter second number: '))

    pro=a*b
    print("product of given number is%d" %(pro))

def div():
    a = int(input("enter first number i: "))
    b = int(input('enter second number: '))

    rat=a/b
    print("ratio  of given number is%1.0f" %(rat))

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
            add()
        elif ch == 2:
            sub()
        elif ch == 3:
            mul()
        elif ch == 4:
            div()
        elif ch == 5:
            ans = False
        else:
            print("Invalid Choice")
        input("\n\nPress any key......")


if __name__=="__main__":
    menu()
