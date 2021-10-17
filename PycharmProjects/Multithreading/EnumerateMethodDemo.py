from threading import *
import time
def display():
    print(current_thread().name,'...started')
    time.sleep(3)
    print(current_thread().name, '...ended')
print('the number of active thread:',active_count())
t1=Thread(target=display,name='childThread_1')
t2=Thread(target=display,name='childThread_2')
t3=Thread(target=display,name='childThread_3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print('thread name:',t.name)
    print('idenfication number:',t.ident)
    print()
time.sleep(10)
l=enumerate()
for t in l:
    print('thread name:',t.name)
    print('idenfication number:',t.ident)
    print()