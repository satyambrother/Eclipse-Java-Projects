# to check valid mobile number

import re
s=input('enter mobile number')
m=re.fullmatch('[6-9]\d{9}',s)
if m!=None:
    print(s,'is valid mobile number')
else:
    print(s,'is not valid mobile number')