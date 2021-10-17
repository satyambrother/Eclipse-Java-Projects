import re
matcher=re.finditer('\s','a7b@k9j')
for m in matcher:
    print(m.start(),'********',m.group())