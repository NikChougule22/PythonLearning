class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B:

    def __init__(self):
        # super().__init__()  # helps to access/call init/constructor of superclass A
        print("in B init")

    def feature3(self):
        print("Feature 3 is working")


a1 = B()  # Tries to find init/constructor of class B first. If init for B does not exist than
          # it tries to call init of A

class C(A,B):
    def __init__(self):
        super().__init__()  # helps to call init of Class A per MRO (Method Resolution Order) which goes from
        # left to right as A is mentioned to left of B in C(A,B)
        print("in C init")

    def feat(self):
        super().feature2()


c1 = C()   # Calls init of A because of super().__init__() in class C, and also prints the C init statement
c1.feat()  # super().feature2 helps to access all methods of superclass A
