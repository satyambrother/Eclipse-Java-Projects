from threading import *
import threading
class Test:
 def display(self):
    for i in range(5):
        print('child thread')
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(5):
  print('main thread')