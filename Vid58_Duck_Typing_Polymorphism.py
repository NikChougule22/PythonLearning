class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):   # ide acts as second object or second self
        ide.execute()

ide1 = PyCharm()    # argument for object which can be passed to method of a class

l1=Laptop()
l1.code(ide1)

ide1 = MyEditor()
l1=Laptop()
l1.code(ide1)

# Thus it doesn't matter which class object you are passing what matters is the object should have method to execute
# ide object can be called by any class and method
# Since the method execute is same name in both classes and can be used by a object from any other class it is called
# ducktyping