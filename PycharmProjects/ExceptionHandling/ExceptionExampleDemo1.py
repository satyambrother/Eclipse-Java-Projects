
try:
    print('try')

    a=int(input('enter integer'))
    print(10 / 0)
except Exception as e:
      print('Except')
      print(e)

else:
    print('else')
finally:
    print('finally')


'''try:
    print('try')
except :
      print('Except')
else:
    print('else')
finally:
     print('finally')'''