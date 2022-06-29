# Operator Overloading is a thing we do to carryout certain operations on objects
# For example when we call a + b in behind scenes __add__ method is working to carryout the operation of addition
# Similarly if we want to add any objects of a class or perform any other operations on that object we define our own
# methods to carryout the actions we need. This is Operator overloading!

a = 5
b = 6
print(a+b)
print(int.__add__(a,b)) # in back ground when you do a+b the compiler calls int class and does method add
a = '5'
b = '6'
print(str.__add__(a,b)) # Adds two strings

# so all operators behind scenes have different methods to do things

# Operator Overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other): # We are over loading operator add to add two objects of student class
        a1=self.m1+other.m1  # adding two students marks so that they can go to s3
        a2=self.m2+other.m2  # adding two students marks so that they can go to s3
        s3=Student(a1,a2)    # defining the new added mark to s3 object
        return s3

    def __gt__(self, other): # Over loading operator greater than equal to compare the objects of student class
        t1=self.m1+self.m2
        t2=other.m1+other.m2
        if t1>t2:
            return True
        else:
            return False

    def __str__(self):   # Over loading Operator String (__str__)
        return '{} {}' .format(s3.m1,s3.m2)

s1=Student(56,35)
s2=Student(63,30)

s3=s1+s2
print(s3.m1,s3.m2)

print(s3.__str__())

if s1>s2:
    print('S1 Wins')
else:
    print('S2 wins')



