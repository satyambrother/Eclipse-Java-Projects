import gc
import sys
import time
class Test:
    def __init__(self):
        print('object initilization')
    def __del__(self):
        print('fullfill last wish and perform cleanup activity')
# Note 1
t1=Test()
t1=None
time.sleep(10)
print('end of the application') # Here both t1 is present but not used

# Note 2
t1=Test()
del t1
#print(t1)  # Here t1 is lost

# Note 3
gc.disable()
print(gc.isenabled())
t1=Test()
t1=None
time.sleep(10)
print('end of the application')

'''1==>garbage collector is disable but still cleanup activity perform.
   it is done because behaviour of the garbage collector is varried
   from plateform to plateform 
    
    2==>The purpose of destructor to perform cleanup activity before 
        destroying object by garbage collector 
                                                '''
