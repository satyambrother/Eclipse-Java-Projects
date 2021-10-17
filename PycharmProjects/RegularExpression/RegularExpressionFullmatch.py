import re
s=input('enter pattern to check:')
m=re.fullmatch(s,'abcdefgh')
if m!=None:
    print('full String match')

else:
    print('full string not match')