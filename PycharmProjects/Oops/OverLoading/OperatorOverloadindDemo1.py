class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,others):      # variable name change according to programming requirement
        return self.pages+others.pages
b1=Book(100)
b2=Book(200)
b3=Book(300)

print(b1+b2) # valid

#print(b1+b2+b3) not valid