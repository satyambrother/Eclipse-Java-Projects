import os
fname=input('enter file name ')
if os.path.isfile(fname):
    print('file exist',fname)
    f=open('output.txt','r')
    print('content of the file is:')
    print(f.read())
else:
    print('file not exist:',fname)