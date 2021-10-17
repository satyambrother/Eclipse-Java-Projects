import logging
logging.basicConfig(filename='log.txt',level=logging.INFO)
logging.info('a new request come')
try:
    x=int(input("enter first number "))
    y=int(input("enter second number: "))
    print(x/y)
except ZeroDivisionError as e:
    print('cannot divisible by zero')
    logging.exception(e)
except ValueError as e:
    print('enter only int value')
    logging.exception(e)
logging.info('request processing complete')