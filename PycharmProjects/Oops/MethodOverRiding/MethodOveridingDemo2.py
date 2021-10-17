class P:
    def property(self):
        print('Cash +Land+Gold')
    def marry(self):
        print('Deepak marrige fix with suchitra')

class C(P):
    def marry(self):
        #super().marry()  # if deepak want to marry with both parent choise and awn choise gharvali and bahrvali
        print('Deepak  marrige fix with parkvali se')

c=C()
c.property()
c.marry()


