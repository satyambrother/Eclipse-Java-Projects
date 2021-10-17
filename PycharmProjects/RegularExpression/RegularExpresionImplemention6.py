import re
s=input('enter registration number')
m=re.fullmatch('up[0-7][0-9][a-z]{2}\d{4',s)
if m!=None:
    print('valid number')
else:
    print('invalid number