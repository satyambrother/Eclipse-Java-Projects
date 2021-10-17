def info(arg,*variable):
    print('output is');
    print(arg);
    for var in variable:
        print(var);
    return

info(10);
info(10,20,30,40);