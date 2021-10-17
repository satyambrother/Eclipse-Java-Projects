import re
s=input('enter pattern to check:')
m=re.search(s,'abcdefgh')
if m!=None:
    print('match is available at  string')
    print('start index:{} and end index: {}'.format(m.start(),m.end()))

else:
    print('full string not match')