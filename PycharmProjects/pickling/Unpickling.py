import emp,pickle
f=open('emp.dat','rb')
print('employee detail')
while True:
    try:
      obj=pickle.load(f)

      print(obj.display(),end='')
    except EOFError:
      print('all employee completed')
      break
f.close()