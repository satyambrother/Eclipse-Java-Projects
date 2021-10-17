import re
matcher=re.finditer('\d','a7bk9z6')
for m in matcher:
    print(m.start(),'***',m.group())