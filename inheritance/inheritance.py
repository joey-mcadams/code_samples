# This is just a dumb example to test a really awful concept.

class A():
    a = 1

    def test(self):
        print("A")


class Mixin1():
    def test(self):
        print("Mix1")


class Mixin2():
    def test(self):
        print("Mix1")


class BaseTest(Mixin1, Mixin2):
    pass


A.a = 2

print(A.a)
BaseTest().test()



