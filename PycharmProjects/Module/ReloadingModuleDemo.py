import time
from imp import reload
import module
print('program enter into sleeping state')
time.sleep(30)
reload(module)
print('this is the last line of the program')