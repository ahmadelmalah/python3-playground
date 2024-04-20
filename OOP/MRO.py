class A:
    @classmethod
    def hello(self):
        print("A Class")


class B(A):
    pass


class C:
    def hello(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.hello()
