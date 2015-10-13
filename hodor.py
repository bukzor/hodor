"""hodor"""
# pylint:disable=invalid-name
from __future__ import print_function


def metaclass(cls, mcs):
    "py2/py3 compat, hodor"
    return mcs('hodor', cls.__bases__, dict(vars(cls)))


class hodor(type):
    """hodor"""
    def __repr__(cls):
        return 'hodor'

    def __call__(cls, *args):
        return cls

# hodor!
hodor = metaclass(hodor, hodor)
hodor.__class__ = hodor  # hodor.

import operator
for op, val in vars(operator).items():
    if not op.startswith('__') or isinstance(val, str):
        continue
    setattr(hodor, op, hodor)
    setattr(hodor, op.replace('__', '__r', 1), hodor)

for op in ('getattr', 'setattr', 'delattr'):
    setattr(hodor, '__%s__' % op, hodor)

# hodor...
import sys
sys.modules[__name__] = hodor

__all__ = ('hodor',)
