# read data from input.txt and write on output.txt
f1=open('input.txt')
f2=open('output.txt','w')
f2.write(f1.read())
f2.close()
print('daa copied from f1 to f2')