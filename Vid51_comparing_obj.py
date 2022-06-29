class Computer:
    def __init__(self):
        self.name = "Nikhil"
        self.age = 29

    def compare(self, other):  # if second variable(other) is placed next to self in a method/function it acts
        # as self for 2nd object present in program, like c1.compare(c2) has self=c1 and other=c2
        if self.age == other.age:
            return True
        else:
            return False

    def update(self):
        self.age = 30


c1 = Computer()
c2 = Computer()

print(c1)  # c1 is a object of computer
print(id(c1))  # seeing the heap memory register where it gets stored
print(c2)

if c1.compare(c2):  # Here c1 will become self in method/function compare and c2 will become other in method or
    # function compare
    print("They are of same age")
else:
    print("They are not of same age")

c2.update()
print("Age of c2 now is:", c2.age)

if c1.compare(c2):  # Here c1 will become self in method/function compare and c2 will become other in method or
    # function compare
    print("They are of same age")
else:
    print("They are not of same age")
