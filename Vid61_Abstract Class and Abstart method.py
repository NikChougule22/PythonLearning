# Abstract method is used when you have a class that is abstract. You can not create instance/Object for abstract class
# If the abstract class has a abstract method then the same method needs to be compulsorily used in derived class
# from abstract class or else you will get error that the derived class can not be instantiated


from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        #    print("Running")
        pass  # declaring a method (Method doesn't have anything


# This method is called as abstract method as it is only declared and has no definition
# com = Computer()  # we can not instantiate an abstact class Computer with abstract method process so it gives error
# com.process()

class desktop(Computer):
    pass  # here we are creating inheriting class from abstract class and again having no method


# this will give the same error that we can not instantiate abstract class with abstract method
# com1=desktop()

# Now
class Laptop(Computer):
    def process(self):  # the Laptop class is inherited from abstract class but has a method that is not abstract
        print("Running")  # so this will generate output

    def printing(self):
        print("I am doing something")


com1 = Laptop()
com1.process()  # this works, that means we can create inherited classes from abstract class and they will work if
# the method is defined. If the method of Laptop would have been also passed and thus would have been abstract then
com1.printing()


class whiteboard(Computer):
    def process(self):
        print(" we need this always included as it is abstract class")

    def write(self):
        print("its writing")


class programmer:
    def work(self, com):  # com acts as second object which can be used with any methods from any other class
        print("solving bugs")
        com.process()
        com.printing()


prog1 = programmer()
prog1.work(com1)  # duck typing used

prog2 = whiteboard()
prog2.write()
