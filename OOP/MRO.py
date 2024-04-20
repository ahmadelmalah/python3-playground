class A:
    def hello(self):
        print("A")


class B(A):
    pass


class C:
    def hello(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.hello()
