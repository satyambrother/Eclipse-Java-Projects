from threading import *
import time
def double(number):
    for n in number:
        time.sleep(1)
        print('Double :',2*n)
def square(number):
    for n in number:
        time.sleep(1)
        print('square',n*n)

number=[10,20,30,40,50]
begintime=time.time()
t1=Thread(target=double, args=(number,))
t2=Thread(target=square,args=(number,))
t1.start()
t2.start()
t1.join()
t2.join()

endtime=time.time()
print('the total time taken: ',endtime-begintime)