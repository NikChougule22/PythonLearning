class Student:
    school = 'A B P E S'  # Class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance method
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # get method or instance method
        return self.m1

    def set_m1(self, value):  # set method or instance method
        self.m1 = value

    @classmethod  # class method
    def getschool(cls):
        return cls.school

    @staticmethod  # static method
    def info():
        print("This is a static method.....")


s1 = Student(23, 42, 56)
s2 = Student(41, 63, 31)

print(s1.avg())
print(Student.getschool())  # class method works with class
print(s1.getschool())  # class method works with all objects as well
Student.info()  # static method does not need class or object
