def f1():
    if __name__=='__main__':
        print('the code executed directly as aprogram')
        print('the value of __name__ is',__name__)
    else:
        print('the code executed indirectly as a module from some other program')
        print('the vale of __name__: ',__name__)
f1()