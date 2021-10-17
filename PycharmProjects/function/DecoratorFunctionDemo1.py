
'''bride==>beautipar==>heroine

input function==>Decorator Function==> output function with extended functionality

note--> Decorator help to make our codeshorter and more pythonic

like new code 10k...existing function is already there 9900 '''

def decor(func):
    def inner(name):
        if name=='sunny':
           print('hello sunny bad morning')
        else:
            func(name)
    return inner
'''@decor
def wish(name):
    print("hello",name,'good morning') #execute both decorator and function simultaneously
wish('satyam')
wish('sunny')
wish('bunny')'''

def wish(name):
    print("hello",name,'good morning')
decorfunction=decor(wish)

wish('satyam')
decorfunction('satyam')  # here execute decorator and function according to choise
print()
wish('sunny')
decorfunction('sunny')