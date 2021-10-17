import re
count=0
#pattern=re.compile('ab')
#matcher=pattern.finditer('abaababa')
matcher=re.finditer('ab','abaaababa')
for m in matcher:
    count+=1
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
    print('number of occurence:',count)