from .base import Op, Op_partial


def _if(x, a, b):
    if x: return a
    return b

@Op
def _print(x):
    print(x)
    return x

@Op_partial(0)
def _dot(x, method):
    return getattr(method)(x)
