from .base import Op

# other not related functions that i like to load together
def _if(x, a, b):
    if x: return a
    return b

def _print(x):
    print(x)
    return x

@Op
def _dot(method, x):
    return getattr(method)(x)
