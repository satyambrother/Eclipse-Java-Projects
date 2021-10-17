from zipfile import*
f=ZipFile('zipfile.zip','r',ZIP_STORED)
names=f.namelist()
for name in names:
    print('file name:',name)
    print('content of the file is :')
    f1=open(name,'r')
    print(f1.read())
    print('*'*10)