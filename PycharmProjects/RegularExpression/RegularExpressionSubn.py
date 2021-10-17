#t=re.subn(regex,replacement,targetStr)
import re
t=re.subn('\d','xx','a7b9k5t9k')
print('the result string:',t[0])
print('the number of replacement:',t[1])