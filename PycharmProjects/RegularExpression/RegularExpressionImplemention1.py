import re
s=input('enter identifier for validation')
m=re.fullmatch('[0-k][0369][0-zA-Z0-9#]*',s)
if m!=None:
    print(s,'is valid javaIdentifier')
else:
    print(s,'is not valid java identifier')