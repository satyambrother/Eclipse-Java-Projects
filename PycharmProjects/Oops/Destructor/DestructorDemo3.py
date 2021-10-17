import gc
import sys
import time
class Test:
    def __init__(self):
        print('object initilization')
    def __del__(self):
        print('fullfill last wish and perform cleanup activity')

list=[Test(),Test(),Test(),Test(),Test()]
time.sleep(5)
list=None
time.sleep(5)
print('end of the file')