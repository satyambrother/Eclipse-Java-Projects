from threading import *
import time
def display(): 
    for i in range(10):
      print('seeta thread')
      time.sleep(3)

t1=Thread(target=display,name='childThread_1')
t1.start()

t1.join(10)
for i in range(10):
    print('rama thread')