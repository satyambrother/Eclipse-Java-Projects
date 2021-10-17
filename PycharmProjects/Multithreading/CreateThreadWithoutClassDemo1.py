from threading import *
import threading
def display():
    print('this code display function executed by thread: ',threading.current_thread().getName())
t=Thread(target=display)
t.start()
print('this code display function executed by thread',threading.current_thread().getName())