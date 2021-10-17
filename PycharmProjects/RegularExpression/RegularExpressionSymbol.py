import re
s='learn python is very easy!!!'
res=re.search("easy$",s)
if res!=None:
    print('target string end with easy')
else:
    print('target string not end with easy')

