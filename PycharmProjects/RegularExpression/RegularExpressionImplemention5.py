import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/info/contact')
text.u.read()
number=re.findall('[0-9]{3}[-][0-9]{8}'.str(text))
for n in number:
    print(n)