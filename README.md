HODOR
=====

For any operation, `hodor` will always say `hodor`.


    >>> from hodor import hodor
    >>> hodor + 1
    hodor
    >>> 3 ** hodor
    hodor
    >>> hodor().foo['bar']
    hodor

What's more, hodor is a module, and a class.

    >>> import hodor
    >>> hodor
    hodor

    >>> class myclass(hodor):
    ...     pass
    >>> myclass()
    hodor

Hodor is also a metaclass!

    >>> myclass
    hodor

    >>> type(myclass)
    hodor


My favorite: hodor is an instance of *itself*.

    >>> type(hodor)
    hodor

    >>> type(hodor) is hodor
    True

Hodor works equally well in python2 and python3.
