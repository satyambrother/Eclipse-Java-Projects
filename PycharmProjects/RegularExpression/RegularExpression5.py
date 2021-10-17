import re
matcher=re.finditer('a*','abaabaab')
for m in matcher:
    print(m.start(),'****',m.group())