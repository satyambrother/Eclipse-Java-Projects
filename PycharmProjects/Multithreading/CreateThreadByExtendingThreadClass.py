from threading import *
import threading
class MyThread(Thread):
   def run(self):
      for i in range(5):
          print('child thread')

t=MyThread()
t.start()
for i in range(5):
  print('main thread')