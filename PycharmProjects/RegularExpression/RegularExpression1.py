import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for match in matcher:
    count+=1
    print('match is available at start index:',match.start())
print('the number of occurence is: ',count)