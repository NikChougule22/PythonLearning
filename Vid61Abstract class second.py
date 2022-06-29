# Abstract method is used when you have a class that is abstract. You can not create instance/Object for abstract class
# If the abstract class has a abstract method then the same method needs to be compulsorily used in derived class
# from abstract class or else you will get error that the derived class can not be instantiated

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def __area__(self):
        pass
    def __perimeter__(self):
        pass

class square(shape):
    def __init__(self,side):
        self.side=side

    def __area__(self):
        area=self.side*self.side
        return area

    def __perimeter__(self):
        perimeter=4*self.side
        return perimeter

sq=square(3)
print(sq.__area__())
print(sq.__perimeter__())








