# A -> B -> C
# MRO


class A:
    def foo(self):
        print("I am in A")


class B(A):
    def foo(self):
        print("I am in B")


class C(A):
    def foo(self):
        print("I am in C")


class H(A):
    pass


class D(B, C, H):
    def foo(self):
        super(C, self).foo()


D().foo()

D.__mro__
