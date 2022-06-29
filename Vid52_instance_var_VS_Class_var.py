class Car:
    Wheels = 4  # Class variable-->Any variables outside init variables are called class variables
    #     # These class variables will always remain same for all variables where as the class variables
    #     # defined within init change with every object based on described for any particular object

    def __init__(self):
        self.com = "Nikhil"  # instance variable
        self.mileage = 29    # instance variable


c1 = Car()
c2 = Car()

print(c1.com, c1.mileage, c1.Wheels)
print(c2.com, c2.mileage, c2.Wheels)

Car.Wheels = 3
print(c1.com, c1.mileage, c1.Wheels)
print(c2.com, c2.mileage, c2.Wheels)
