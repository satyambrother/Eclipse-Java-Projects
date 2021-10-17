from threading import *
import time
def display():
    print(current_thread().name,'...started')
    time.sleep(3)
    print(current_thread().name, '...started')
print('the number of active thread:',active_count())
t1=Thread(target=display,name='childThread_1')
t2=Thread(target=display,name='childThread_2')
t3=Thread(target=display,name='childThread_3')
t1.start()
t2.start()
t3.start()
print('the number of active thread:',active_count())
time.sleep(10)
print('the number of active thread:',active_count())