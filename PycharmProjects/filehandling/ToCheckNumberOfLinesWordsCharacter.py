import os
fname=input('enter file name:')
if os.path.isfile(fname):
    print('file exist:',fname)
    f=open('example2.txt','r')
    lcount=wcount=ccount=0
    for line in f:
        lcount=lcount+1
        words=line.split()
        wcount=wcount+len(words)
        ccount=ccount+len(line)
    print('the number of lines:',lcount)
    print('the number of word:',wcount)
    print('the number of characte',ccount)

else:
    print('file not exist:')


