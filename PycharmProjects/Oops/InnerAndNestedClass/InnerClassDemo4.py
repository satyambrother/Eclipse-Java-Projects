class Human:
    def __init__(self):
        self.name='satyam'
        self.head=self.Head()
    def display(self):
        print('Name: ',self.name)
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            self.brain=self.Brain()
        def talk(self):
            print('talking')
        class Brain:
            def think(self):
                print('thinking')

h=Human()
h.display()