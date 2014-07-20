# pylint:disable=invalid-name,too-few-public-methods,missing-docstring,no-init
from __future__ import print_function
from hodor import hodor, metaclass

print(hodor)
print(hodor.x)
print(hodor())
print(type(hodor))

print(hodor(1))
print(hodor(1, 2))
print(hodor(1, 2, 3))
print(hodor(1, 2, 3, 4, 5))

print(hodor + hodor)
print(hodor.__add__)
print(pow(hodor, hodor, hodor))

print(1 + hodor)
print(hodor + 1)
print(hodor << 1)
print(1 << hodor)
print(hodor[1])


class myobj(hodor):
    pass

print(myobj)
print(myobj())

myobj2 = metaclass(object, hodor)

print(myobj2)
print(myobj2())
