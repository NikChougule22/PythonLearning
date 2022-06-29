class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == 'Tennis Player':
            print(self.name, 'plays Tennis')
        elif self.occupation == 'actor':
            print(self.name, 'Shoots Films')

    def speaks(self):
        print(self.name, 'Says how are you?')


tom = Human('Tom Cruise', 'actor')
tom.do_work()
tom.speaks()
