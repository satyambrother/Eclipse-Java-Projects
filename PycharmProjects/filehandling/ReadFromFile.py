f=open('example2.txt','r')
#data=f.read()
#print(data,end='')

#data1=f.read(10)
#print(data1)

#line=f.readline()
#print(line)

line1=f.readlines()
for line in line1:
     print(line,end='')