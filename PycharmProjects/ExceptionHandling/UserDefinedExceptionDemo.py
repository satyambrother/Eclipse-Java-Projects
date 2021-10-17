class ToYoungException(Exception):
     def __init__(self,arg):
         self.arg=arg
class ToOldException(Exception):
      def __init__(self,arg):
          self.arg=arg
age=int(input('enter age: '))
if age>60:
    raise ToOldException("your age is already crossed")
elif age<18:
    raise ToYoungException('please wait some time to get best match')
else:
    print('you get best match soon on your mail')