import re
s=input('enter pattern to check:')
m=re.match(s,'abcdefgh')
if m!=None:
    print('match is available at the begnining of the string')
    print('start index:{} and end index: {}'.format(m.start(),m.end()))

else:
    print('match is not available at the begin og the start')