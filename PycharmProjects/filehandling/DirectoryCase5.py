'''ort os
print(os.listdir('.')'''

'''import os
list=os.listdir()
for name in list:
    print(name)'''

'''import os
list=os.listdir('E://')
for name in list:
    print(name)
    
print('total number of directory and file in path:',len(list)) '''

import os
for dirpath,dirnames,dirfiles in os.walk('.'):
    print('cwd:',dirpath)
    print('Directory:',dirnames)
    print('filename',dirfiles)
    print()
