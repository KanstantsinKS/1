class A:
    def method(self):
        print('method of class A')

class B(A):
    def method(self):
        print('method of class B')

class C(A):
    def method(self):
        print('method of class C')

class D(B, C):
    def method(self):
        print('method of class D')


# __mro__, mro, help(class)
print(D.__mro__)
print(D.mro())
help(D)