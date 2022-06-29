# Method over loading  is where if in a class there are two methods of same name but different arguments
# or parameters it is called Mehod over loading
# For example if student class has two methods average and one takes two arguments and other takes 3 arguments

# Method Over Loading
# Python does not have method overloading but we can use tricks to do method overloading
# Suppose we want to use a method which has three arguments defined but we want to use only 2 arguments out of it

class student:

    # def sum(self,a,b):
    #     s=a+b
    #     return s

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

s1=student()
print(s1.sum(5,6))
# if we do print(s1.sum(5,6,9))  it will give us error that student.sum or sum method takes only 3 arguments (self,a,b)
# but 4 arguments were given. In other languages in such cases you will just make new sum class with 3 arguments
# sum(self,a,b,c) and it will work as method over loading but in python we will have to do following:

print(s1.sum(5,6,9))

# Method Over riding

class A:
    def show(self):
        print('In Class A')

class B(A):
    def show(self):    # The Show() method in class B overrides the inheritated method show from class A
        print('In Class B')


a1=A()
a1.show()
b1=B()
b1.show()
