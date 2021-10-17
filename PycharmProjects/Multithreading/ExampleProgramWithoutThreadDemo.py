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
double(number)
square(number)
endtime=time.time()
print('the total time taken: ',endtime-begintime)