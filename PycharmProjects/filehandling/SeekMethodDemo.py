data='all student are STUPID'
f=open('example2.txt','w')
f.write(data)
with open('example2.txt','r+') as f:
     text=f.read()
     print(text)
     print('current position of the cursor:',f.tell())
     f.seek(17)
     print('current position of the cursor:', f.tell())
     f.write('gems')
     f.seek(0)
     text=f.read()
     print('Data after modification')
     print(text)