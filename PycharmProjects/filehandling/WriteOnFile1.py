f=open('example2.txt','w')
l=['satyam\n','shivam\n','sundram\n','dhan jee']
f.writelines(l)

f.close()
print("write operation completed")