class A:

    def feature1(self):
        print('Feature 1 in working')

    def feature2(self):
        print('Feature 2 in working')


a1 = A()
a1.feature1()


class B(A):  # Class B is inheriting class A as B is inheriting from A

    def feature3(self):
        print('Feature 3 in working')

    def feature4(self):
        print('Feature 4 in working')


b1 = B()
b1.feature1()  # you get all methods from class A


class C(B):  # Class B is inheriting class A
             # class C(B,A): can also be used if A and B are two separate classes

    def feature5(self):
        print('Feature 5 in working')

    def feature6(self):
        print('Feature 6 in working')


c1 = C()
c1.feature2()  # you get all methods from class A and B for C as C is inheriting from B and B is inheriting from A

