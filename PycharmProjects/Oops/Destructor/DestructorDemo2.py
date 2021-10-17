import gc
import sys
import time
class Test:
    def __init__(self):
        print('object initilization')
    def __del__(self):
        print('fullfill last wish and perform cleanup activity')
t1=Test()
t2=t1
t3=t2
t4=t3
del t1
time.sleep(5)
print('After deleting t1 object not destroyed')
del t2
del t3
time.sleep(5)
print('still object not eligible for gc')
time.sleep(5)
del t4
time.sleep(5)
print('end of the file')

'''if any object is pointed by multiple reference then it 
   should not go with garbage collector untill all refernces is not lost'''