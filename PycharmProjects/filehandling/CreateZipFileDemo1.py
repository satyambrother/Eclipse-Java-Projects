from zipfile import*
f=ZipFile('zipfile.zip','w',ZIP_DEFLATED)
f.write('example.txt')
f.close()
print('zipfile created successfully')

