class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walk with {} legs'.format(name,cls.legs))
Animal.walk('dog')
Animal.walk('cow')