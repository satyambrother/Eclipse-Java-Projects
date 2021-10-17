class Book:
    def __init__(self,pages):
         self.pages=pages

    def __str__(self):          # it used to print any object
         return 'the number of pages '+str(self.pages)

    def __add__(x,y):
        total=x.pages+y.pages
        b=Book(total)
        return b

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(700)

print(b1)
print(b1+b2)
print(b1+b2+b3+b4)


