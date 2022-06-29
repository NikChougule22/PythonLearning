# define a class
class Computer:
    def config(self):
        print("i5,240GB SSD, 16 GB RAM")

# define object com1 and com2 of class computer
com1 = Computer()
com2 = Computer()

# To execute, call class, then which method/function of class and finally object name of that method
Computer.config(com1)
Computer.config(com2)

# Shortcut to call by just mentioning first object. Since object com1 belongs to a particular class here Computer
# it automatically selects class and so we do need to mention class name. Also the object automatically gets called
# in config brackets i.e here com1 goes as a object attribute to method config
com1.config()   # doing same as line above 11
com2.config()
