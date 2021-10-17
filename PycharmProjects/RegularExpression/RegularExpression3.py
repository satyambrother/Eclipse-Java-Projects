import re
matcher=re.finditer('[abc]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())