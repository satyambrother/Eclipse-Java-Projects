
from threading import *
print(current_thread().getName())
current_thread().setName('satyam')
print(current_thread().getName())
