import re.urllib
import urllib.request
sites=['http://google.com','http://rediff.com']
for s in sites:
    print('searching',s)
    u=urllib.request.urlopen(s)
    text.u.read()
    title=re.findall("<title>*</title>",str(text),re.IGNORECASE)
    print(title[0])