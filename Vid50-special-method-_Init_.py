class Computer:
    # define variables
    def __init__(self, CPU, RAM):  # init is used to initialize variables/arguments and is also called constructor
        # we are going to use two variables/arguments CPU and RAM for the object com1

        self.CPU = CPU  # CPU is var/arg of object com1, and so CPU always goes with object com1, so while defining
        # we define by using self.CPU, because we might want to use same variable for different
        # objects like com2 so we use self, and self takes place of object along with variable
        # example com1.CPU, com2.CPU

        self.RAM = RAM

    # define method/function
    def config(self):
        print("Config is:", self.CPU, self.RAM)


com1 = Computer('i5', 16)  # giving actual value/name to variables for object 1
com2 = Computer('Razen', 10)

com1.config()
com2.config()

# Thus we have global variables/arguments (CPU,RAM) and global methods/functions (config()) defined in a class
# which can be used by multiple objects having its own variable values which get assigned in global class variables
# and do the required action in global class methods
