class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # create object of inner class Laptop inside outer class Student

    def Show(self):
        print(self.name, self.rollno)
        self.lap.show()  # call the inner class 'Laptop' method 'show' in outer class 'Student' method 'Show'

    class Laptop:  # Inner class laptop in outer class Student

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Navin', 25)
s2 = Student('Nikhil', 27)

s1.Show()
s2.Show()