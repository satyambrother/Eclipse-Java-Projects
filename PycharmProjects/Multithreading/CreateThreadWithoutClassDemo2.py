from threading import *
import threading
def display():
    for i in range(5):
        print('child thread')
t=Thread(target=display)
t.start()
for i in range(5):
  print('main thread')