# file name taken as dynamically
fname=input('Enter file name:')
f=open(fname,'w')
feedback=input('Enter your feedback')
f.write(feedback)
f.close()
print('enter feedback successfully')